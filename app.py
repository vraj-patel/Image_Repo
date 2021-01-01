from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import text_search as Text_Search
import image_search as Image_Search
import os
import zipfile

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

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
  image_file.save('./myimage.jpg')
  return jsonify({"message": 'success'})


if __name__ == '__main__':
  app.run(debug=True)