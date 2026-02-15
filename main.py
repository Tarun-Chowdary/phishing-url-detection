# main.py

from src.feature_extractor import extract_features
from src.model_loader import load_model

def main():
    print("=== Phishing URL Detection System ===")

    model = load_model()

    while True:
        url = input("\nEnter URL (or type 'exit' to quit): ")

        if url.lower() == "exit":
            break

        features = extract_features(url)
        prediction = model.predict(features)[0]

        if prediction == 1:
            print("⚠️  Phishing URL Detected")
        else:
            print("✅ Legitimate URL")

if __name__ == "__main__":
    main()
