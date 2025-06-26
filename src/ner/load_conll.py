# Load and parse CoNLL format

# src/ner/load_conll.py

# def read_conll_file(filepath):
#     sentences, labels = [], []
#     with open(filepath, 'r', encoding='utf-8') as f:
#         sentence, label = [], []
#         for line in f:
#             line = line.strip()
#             if not line:
#                 if sentence:
#                     sentences.append(sentence)
#                     labels.append(label)
#                     sentence, label = [], []
#             else:
#                 token, tag = line.split()
#                 sentence.append(token)
#                 label.append(tag)
#     return sentences, labels

def read_conll_file(filepath):
    sentences, labels = [], []
    with open(filepath, 'r', encoding='utf-8') as f:
        sentence, label = [], []
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                if sentence:
                    sentences.append(sentence)
                    labels.append(label)
                    sentence, label = [], []
            else:
                parts = line.split()
                if len(parts) == 2:
                    token, tag = parts
                    sentence.append(token)
                    label.append(tag)
                else:
                    print(f"⚠️ Skipping malformed line {line_num}: {line}")
    return sentences, labels
