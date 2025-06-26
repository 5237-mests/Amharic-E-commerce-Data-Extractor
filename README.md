## 📄 `README.md` for KAIM Week 4 Project

# 📦 Amharic E-commerce NER System for EthioMart

This project is part of **10 Academy KAIM Week 4**, focused on developing a transformer-based **Named Entity Recognition (NER)** system for extracting structured business data (Product, Price, Location) from unstructured **Amharic Telegram messages**.

The end goal is to help **EthioMart**:

- Centralize e-commerce product listings from Telegram
- Score vendors for **micro-lending opportunities**

---

## 🚀 Project Highlights

- ✅ Custom **Telegram scraper** (via Telethon)
- ✅ Amharic text **preprocessing and normalization**
- ✅ CoNLL-format **NER dataset creation** (manual labeling)
- ✅ Model fine-tuning using Hugging Face (`XLM-R`, `BERT-Amharic`, etc.)
- ✅ **SHAP/LIME** for model interpretability
- ✅ Vendor scoring system for **FinTech insights**

---

## 📂 Project Structure

├── data/
│ ├── raw/ # Raw scraped Telegram data
│ ├── processed/ # Cleaned text data
│ ├── labeled/ # CoNLL-labeled NER data
│ └── telegram_media/ # Downloaded product images
│
├── notebooks/ # Jupyter notebooks per task
│ ├── 01_data_ingestion.ipynb
│ ├── 02_preprocessing.ipynb
│ ├── 03_labeling.ipynb
│ └── ...
│
├── src/
│ ├── scraping/telegram_scraper.py
│ ├── preprocessing/clean_text.py
│ └── fintech/scorecard.py
│
├── scripts/ # Helper scripts (e.g., CoNLL labeling)
├── models/ # Fine-tuned model files and metrics
├── reports/ # Interim and final PDF reports
├── streamlit_app.py # (Optional) Web app UI
├── config.yaml # API keys, model config
├── README.md
└── requirements.txt

---

## 📊 NER Entity Types

| Entity     | Example                  |
| ---------- | ------------------------ |
| `Product`  | "vaporfoam", "cake rack" |
| `Price`    | "3000 ብር", "Price 2000"  |
| `Location` | "አዲስ አበባ", "ቦሌ"          |

Annotated with the BIO format: `B-Product`, `I-PRICE`, `O`, etc.

---

## 📥 Data Collection

We scraped 1000+ messages from real e-commerce Telegram channels like:

- `@Shageronlinestore`
- `@ZemenExpress`
- `@nevacomputer`

Using an async Telethon-based script and stored them in structured `.csv` and `.json` files.

---

## 🔧 Model Training (Hugging Face)

Fine-tuned multilingual and Amharic-specific models:

- [`xlm-roberta-base`](https://huggingface.co/FacebookAI/xlm-roberta-base)
- [`bert-tiny-amharic`](https://huggingface.co/rasyosef/bert-tiny-amharic)
- [`afroxlmr`](https://huggingface.co/masakhane/afroxlmr-large-ner-masakhaner-1.0_2.0)

Evaluated using:

- F1-score
- Precision, Recall
- Interpretability (SHAP/LIME)

---

## 📈 FinTech Vendor Scorecard

Using metadata + NER outputs to rank vendors by:

- 📅 Posting frequency
- 👁️ Avg. views/post
- 💸 Avg. price point
- 🔢 Custom **Lending Score**

Final table helps EthioMart offer **micro-loans** to top-performing vendors.

---

## 📚 Reports

- `reports/interimreportweek4.pdf` – Ingestion + labeling phase
- `reports/final_report_week4.pdf` – Full pipeline, evaluation & business impact

---

## 🧠 Tech Stack

- Python, Pandas, Regex
- Telethon (Telegram scraping)
- Hugging Face Transformers + Datasets
- Jupyter, Google Colab
- SHAP, LIME

---

## 📌 Author

**Mesfin Mulugeta**
10 Academy – KAIM Week 4
📧 [msfnmulgeta@gmail.com](mailto:msfnmulgeta@gmail.com)
🔗 [LinkedIn](https://linkedin.com/in/mesfin-mulgeta) | [GitHub](https://github.com/5237-mests)

---
