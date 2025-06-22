import pandas as pd
import re

def tokenize_amharic_text(text):
    """Simple whitespace and punctuation-aware tokenizer"""
    if not isinstance(text, str):
        return []
    # Remove phone numbers, urls, emojis, then split
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[።፡]', ' ', text)
    return text.strip().split()

def generate_conll_template(input_csv, output_txt):
    df = pd.read_csv(input_csv)
    texts = df['Cleaned Text'].dropna().tolist()

    with open(output_txt, 'w', encoding='utf-8') as f:
        for text in texts:
            tokens = tokenize_amharic_text(text)
            for token in tokens:
                f.write(f"{token} O\n")  # All tokens initially marked as 'O'
            f.write("\n")  # Blank line between sentences

    print(f"✅ CoNLL template created at: {output_txt}")

if __name__ == "__main__":
    input_csv_path = "../data/labeled/sample_for_labeling.csv"
    output_conll_path = "../data/labeled/ner_data.conll"
    generate_conll_template(input_csv_path, output_conll_path)
