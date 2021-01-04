# Image_Repo

This image repository project, created with **Python**, **Flask** and **SQL**, provides endpoints to:

- search image by text
- search image by characteristics
- search image by another image
- upload image

To perform image search, **Machine Learning**, **Deep Learning**, and **NLP** techniques are used (explained below).

The Flicker8k image captioning dataset was used to train the deep learning models. The dataset is too large to be included and I do not own this data. Fill out the following form to download the dataset: [Form](https://forms.illinois.edu/sec/1713398).

To run the project or to run the machine learning tasks, follow the steps listed below.

## Machine Learning and Generating Captions

When uploading an image, if a caption (description of the image) is not passed as form-data, the `/Image_Captioning` directory will automatically generate a caption. This way, if no caption is provided, this repo can still perform text based search.

This is done by using a Convolutional Neural Network (CNN) to extract and encode features from the image, as commonly done by other computer vision projects, and uses a Recurrent Neural Network (RNN) to decode features to form a description of the image. VGG16 is a pre-trained CNN based model used to encode the features. A RNN is trained to greedily generate a sequence of words to form the caption. Inspiration for this (sub)project was taken from Jason Brownlee's blog post on image captioning.

Since training a RNN is a cumbersome and memory intensive process, the tokenizer and extracted features file are provided in the `/Image_Captioning` directory. Optimized model(s) are provided in `/final_ml_models`.

## Steps to Run this Project

1. Create folders named `image_features` and `images` in `/Upload_Folder`
2. Make sure you have installed and are using python3 and pip3
3. Install pipenv: `pip3 install pipenv`
4. Start pipenv shell: `pipenv shell`
5. Install all required packages as listed in Pipfile: `pipenv install`
6. In the pipenv shell, start app.py: `python3 app.py`
7. Either use the `/upload` endpoint OR manually upload images in the `/Upload_Folder/images` directory, along with a descriptions.txt file with image filenames and captions/descriptions as shown in `/Upload_Folder/descriptions.txt`
8. If you manually inserted the images, open a separate terminal, `cd Upload_Folder`, and run `python3 extract_all.py`
9. Start hitting the endpoints! The search results will be returned as a zip file (response) and also saved to the `/Search_Results` directory

## Steps to Train an Image Captioning Model

1. Download the flickr8k dataset (using the form provided above) and place all images in `/Image_Captioning/Flicker8k_Dataset`. Place all the .txt files provided with the dataset in Flickr8k_text.
2. Run all python files in /Image\*Captioning in order ("1*.py", "2*.py", ...) to generate 20 models (1 for each epoch) and choose the one which produces the least loss as your final model. Place the final model in `/final_ml_models`.
