from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy 
import text_search as Text_Search
import image_search as Image_Search
import os
import zipfile
import uuid
from werkzeug.utils import secure_filename
import json
import Upload_Folder.extract_features as Extract_Features
import Image_Captioning.Generate_Caption as Caption_Generator

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///image_repo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Captions(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  image_id = db.Column('image_id', db.String)
  caption = db.Column('caption', db.String)

class Characteristics(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  image_id = db.Column('image_id', db.String, nullable=False)
  subject = db.Column('subject', db.String, nullable=False)
  subject_colours = db.Column('subject_colours', db.String, nullable=True)
  subject_actions = db.Column('subject_actions', db.String, nullable=True)

@app.route('/text_search', methods=['POST'])
def text_search():
  txt = request.json['text_query']
  all_files = Text_Search.search(txt)
  zipped = zipfile.ZipFile('./Search_Results/text_search_results.zip', 'w')
  for file in all_files:
    zipped.write('Search_Results/'+file)
  zipped.close()
  return send_from_directory('./Search_Results', 'text_search_results.zip')

@app.route('/image_search', methods=['POST'])
def image_search():
  image_file = request.files['image_query']
  image_file.save('./image_query.jpg')
  all_files = Image_Search.search('image_query.jpg')
  zipped = zipfile.ZipFile('./Search_Results/image_search_results.zip', 'w')
  for file in all_files:
    zipped.write('Search_Results/'+file)
  zipped.close()
  return send_from_directory('./Search_Results', 'image_search_results.zip')

@app.route('/upload', methods=['POST'])
def upload_image():
  image_file = request.files['image_file']
  provided_caption = request.form['caption'] if 'caption' in request.form else False
  characteristics = json.loads(request.form['characteristics']) if 'characteristics' in request.form else []
  filename_uuid = secure_filename(str(uuid.uuid4()))
  image_file.save('./Upload_Folder/images/' + filename_uuid + '.jpg')
  Extract_Features.extract('./Upload_Folder/images/', filename_uuid + '.jpg', './Upload_Folder/image_features/')
  if provided_caption:
    with open("./Upload_Folder/descriptions.txt", "a") as image_captions_file:
      image_captions_file.write("\n" + filename_uuid + ' ' + provided_caption)
    caption = Captions(image_id=filename_uuid, caption=provided_caption)
    db.session.add(caption)
    db.session.commit()
  else:
    gen_caption = Caption_Generator.get_caption('./Upload_Folder/images/'+ filename_uuid + '.jpg')
    with open("./Upload_Folder/descriptions.txt", "a") as image_captions_file:
      image_captions_file.write("\n" + filename_uuid + ' ' + gen_caption)
    caption = Captions(image_id=filename_uuid, caption=gen_caption)
    db.session.add(caption)
    db.session.commit()
    
  if len(characteristics):
    for char in characteristics:
      colours = " ".join(char['subject_colours']) if 'subject_colours' in char else ""
      actions = " ".join(char['subject_actions']) if 'subject_actions' in char else ""
      db_char = Characteristics(image_id=filename_uuid, subject=char['subject'], subject_colours=colours, subject_actions=actions)
      db.session.add(db_char)
      db.session.commit()

  return jsonify({"message": 'Successfully uploaded image'})

if __name__ == '__main__':
  app.run(debug=True)