# Load model, tokenizer, label mappings

# src/ner/model_setup.py

from transformers import AutoTokenizer, AutoModelForTokenClassification

def load_model_and_tokenizer(model_name, num_labels):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained(model_name, num_labels=num_labels)
    return tokenizer, model
