# Malicious URL Detection using Random Forest 
This notebook was written to apply some machine learning concepts I have learned, as well as an introduction to computer security.

Using a dataset containing a list of URLs sorted into two categories: benign or malicious, the model is trained on that data after some cleaning and preprocessing, before being evaluated using a train-test split and a Random Forest classifier.

Trained a Random Forest classifier on 6,000 URLs to detect malicious links with a recall of 0.88 for malicious URLs.

The Kaggle notebook link is here: [Malicious URL Detector](https://www.kaggle.com/code/martintej/malicious-url-detector)

This repository includes the code from the notebook and a standalone Python version.

## Tech Stack
```
Python
pandas
sentence-transformers (BAAI/bge-small-en-v1.5)
scikit-learn (Random Forest)
joblib
```
## How it Works
A full breakdown of the data processing, model choice, training, and evaluation is documented in the Kaggle notebook linked above. 

Here are the results of my third run:

<img width="498" height="220" alt="Screenshot 2026-05-21 231728" src="https://github.com/user-attachments/assets/f31365a7-82ad-4d6b-ad1f-1e76962a9a4b" />

## Sources
* Dataset: [malicious-urls-dataset](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset)
* Model: [scikit-learn Random Forest](https://scikit-learn.org/stable/modules/ensemble.html)
* Data operations: [pandas](https://pandas.pydata.org/)
* Embeddings: [sentence-transformers](https://huggingface.co/sentence-transformers)
* Save model: [joblib](https://joblib.readthedocs.io/en/stable/)
