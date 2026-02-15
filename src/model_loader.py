# src/model_loader.py

import pickle

def load_model():
    with open("model/random_forest_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model
