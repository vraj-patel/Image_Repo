import pytest
import shutil
import Upload_Folder.extract_features as Extract_Features
import os.path
from os import path

image_ids = [
    "1009434119_febe49276a.jpg",       
    "963730324_0638534227.jpg",   
    "968081289_cdba83ce2e.jpg",        
    "974924582_10bed89b8d.jpg",        
    "978580450_e862715aba.jpg",
    "1129704496_4a61441f2c.jpg",       
    "964197865_0133acaeb4.jpg",     
    "970641406_9a20ee636a.jpg",       
    "975131015_9acd25db9c.jpg",
    "895502702_5170ada2ee.jpg",       
    "965444691_fe7e85bf0e.jpg",        
    "972381743_5677b420ab.jpg",       
    "976392326_082dafc3c5.jpg",
    "925491651_57df3a5b36.jpg ",       
    "967719295_3257695095.jpg",        
    "973827791_467d83986e.jpg",        
    "977856234_0d9caee7b2.jpg"
]

def test_existing_uploaded_images():
    for img in image_ids:
        shutil.copyfile('./images/'+img, './uploaded_images/'+img)
        Extract_Features.extract('./uploaded_images/', img, './uploaded_image_features/')
        assert path.exists('./uploaded_images/' + img) and path.exists('./uploaded_image_features/' + img)
