import numpy as np
from PIL import Image
from Upload_Folder.feature_extractor import FeatureExtractor
from datetime import datetime
from flask import Flask, request, render_template
from pathlib import Path
import os
import shutil

def search(search_img_path):

    fe = FeatureExtractor()
    features = []
    img_paths = []
    for feature_path in Path("./Upload_Folder/image_features").glob("*.npy"):
        features.append(np.load(feature_path))
        img_paths.append(Path("./Upload_Folder/images") / (feature_path.stem + ".jpg"))
    features = np.array(features)

    img = Image.open(search_img_path)

    query = fe.extract(img)
    dists = np.linalg.norm(features-query, axis=1) 
    ids = np.argsort(dists)[:10]  
    scores = [(dists[id], img_paths[id]) for id in ids]

    for f in os.listdir('Search_Results'):
        os.remove(os.path.join('Search_Results', f))

    results = []
    
    for score in scores:
        img_name = str(score[1]).split('/')[-1]
        results.append(img_name)
        shutil.copyfile(score[1], './Search_Results/'+img_name)

    return results
