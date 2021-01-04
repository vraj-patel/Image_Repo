from PIL import Image
from . import feature_extractor
from pathlib import Path
import numpy as np

fe = feature_extractor.FeatureExtractor()

def extract(image_path, filename, dir_to_store):
    file_uuid = filename.replace('.jpg', '')
    feature = fe.extract(img=Image.open(image_path+filename))
    feature_path = Path(dir_to_store) / (file_uuid + ".npy")
    np.save(feature_path, feature)