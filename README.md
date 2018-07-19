# Cats-and-Dogs-Classifier
A CNN model to classify cat and dog images

Cats and Dogs classifier using Kaggle's dataset
I have only uploaded a subset of orginal data. You can the complete dataset from this link 
https://www.kaggle.com/c/dogs-vs-cats/data

prep_data.py - Is the file used to preprocess the image and save data as a npz file
train_and_test.ipynb - this is the meat of the code. It splits the data into training and testing sets, builds a network, trains and tests it

If you want to try running the code, Run the prep_data.py first to generate a dataset.npz file and run the code in train_and_test.ipynb after that
