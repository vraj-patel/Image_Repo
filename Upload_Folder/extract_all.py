from PIL import Image
import feature_extractor
from pathlib import Path
import numpy as np

fe = feature_extractor.FeatureExtractor()

for img_path in sorted(Path("./images").glob("*.jpg")):
    print(img_path)
    feature = fe.extract(img=Image.open(img_path))
    feature_path = Path("./image_features") / (img_path.stem + ".npy")
    np.save(feature_path, feature)