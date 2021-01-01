from PIL import Image
from feature_extractor import FeatureExtractor
from pathlib import Path
import numpy as np

fe = FeatureExtractor()

for img_path in sorted(Path("./images").glob("*.jpg")):
    print(img_path)
    feature = fe.extract(img=Image.open(img_path))
    feature_path = Path("./image_features") / (img_path.stem + ".npy")
    np.save(feature_path, feature)