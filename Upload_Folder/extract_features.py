from PIL import Image
from . import feature_extractor
from pathlib import Path
import numpy as np

fe = feature_extractor.FeatureExtractor()

def extract(image_path, filename, dir_to_store):
    file_uuid = filename.replace('.jpg', '')
    feature = fe.extract(img=Image.open(image_path+filename))
    feature_path = Path(dir_to_store) / (file_uuid + ".npy")
    print('--------------', feature_path)
    np.save(feature_path, feature)

def extract_all():
    for img_path in sorted(Path("./images").glob("*.jpg")):
        print(img_path)
        feature = fe.extract(img=Image.open(img_path))
        feature_path = Path("./image_features") / (img_path.stem + ".npy")
        np.save(feature_path, feature)