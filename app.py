from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import text_search as Text_Search
import image_search as Image_Search
import os
import zipfile
import uuid
from werkzeug.utils import secure_filename
import json

"""
Storage Locations:
- images: file system
- captions: database (id is filename, caption)
- characteristics: database (image_path (id), subject name, subject color, subject action)
- pkl feature files: file

Uploading file details
- send file, description(optional), array of characteristics(optional)

"""

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:tiger@localhost/Image_Repo')
# db = SQLAlchemy(app)

# class Image(db.Model):
#   id = db.Column('id', db.Integer, primary_key=True)

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
  image_file.save('./uploaded_image.jpg')
  all_files = Image_Search.search('uploaded_image.jpg')
  zipped = zipfile.ZipFile('./Search_Results/image_search_results.zip', 'w')
  for file in all_files:
    zipped.write('Search_Results/'+file)
  zipped.close()
  return send_from_directory('./Search_Results', 'image_search_results.zip')

@app.route('/upload', methods=['POST'])
def upload_image():
  image_file = request.files['image_file']
  provided_caption = request.form['caption']
  characteristics = json.loads(request.form['characteristics'])
  filename = secure_filename(str(uuid.uuid4())+'.jpg')
  image_file.save('./Upload_Folder/images/' + filename)

  return jsonify({"message": 'Successfully uploaded image'})

if __name__ == '__main__':
  app.run(debug=True)