# ⚖️ Legal Case Finder

> **NLP-Powered Legal Search & Outcome Prediction System**  
> *Vector Space Model • TF-IDF • Cosine Similarity • Naive Bayes*

---

## 📌 Overview

**Legal Case Finder** is a Natural Language Processing (NLP) application designed to analyze and retrieve relevant legal cases from a dataset of **24,000+ Australian Federal Court decisions**.

Users can input a legal scenario in plain English and:

- 🔍 Retrieve **similar past cases** using semantic similarity
- ⚖️ Predict **likely legal outcomes** using machine learning

---

## 🚀 Key Features

- Advanced **text preprocessing pipeline**
- **TF-IDF vectorization** for document representation
- **Cosine Similarity** for case retrieval
- **Naive Bayes classifier** for outcome prediction
- RESTful API built with Flask
- Web interface powered by Node.js + Express

---

## 🧠 What the System Does

### Input:
A legal query in natural language  
Example:
```
copyright infringement of digital content
```

### Output:

| Model                | Functionality | Output |
|---------------------|-------------|--------|
| **Cosine Similarity** | Finds top similar legal cases | Top 5 cases + similarity scores |
| **Naive Bayes**      | Predicts case outcome | Outcome + confidence |

---

## 📊 Dataset

### 📁 Source
- Australian Federal Court legal dataset (CSV format)

### 🧾 Structure

| Column        | Description |
|--------------|------------|
| `case_id`     | Unique identifier |
| `case_outcome`| Legal treatment |
| `case_title`  | Case name |
| `case_text`   | Full judgment text |

---

### ⚖️ Case Outcomes Explained

| Outcome       | Meaning | Strength |
|--------------|--------|---------|
| cited        | Referenced | Weak |
| referred to  | Background reference | Weak |
| applied      | Rule applied directly | Strong |
| followed     | Decision repeated | Strong |
| considered   | Carefully analyzed | Medium |
| discussed    | Explained in detail | Medium |
| distinguished| Compared but not applied | Neutral |

---

### 📈 Dataset Stats

| Metric | Value |
|------|------|
| Total cases (raw) | 24,985 |
| After cleaning | 24,483 |
| Dropped (missing text) | 176 |
| Outcomes used | 7 |
| TF-IDF features | 5,000 |

---

## 🗂️ Project Structure

```
legal_case_finder/
│
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── requirements.txt
│   └── dataset/
│       └── legal_cases.csv
│
└── frontend/
    ├── app.js
    ├── package.json
    └── public/
        └── index.html
```

---

## 🏗️ System Architecture

| Component | Technology | Port | Role |
|----------|-----------|------|------|
| Frontend | Node.js + Express | 3000 | UI |
| Backend  | Python + Flask | 5000 | API |
| Models   | scikit-learn | — | ML logic |
| Dataset  | pandas CSV | — | Data |

---

### 🔄 Request Flow

1. User enters query in browser  
2. POST request sent to backend  
3. Flask processes query  
4. ML models run  
5. JSON response returned  
6. UI displays results  

---

## 🧪 NLP Pipeline

### 1️⃣ Data Loading
- Remove missing texts
- Filter rare outcomes

---

### 2️⃣ Text Cleaning
- Lowercasing
- Remove punctuation (`[^a-z\s]`)
- Remove stopwords (NLTK)

---

### 3️⃣ TF-IDF Vectorization

- Converts text into **5,000-dimensional vectors**
- Highlights **important legal terms**

---

### 4️⃣ Cosine Similarity

- Measures similarity between vectors  
- Range: `0 → 1`

Returns:
- Top 5 closest legal cases

---

### 5️⃣ Naive Bayes Classification

- Multinomial model
- Train/Test split: 80/20
- Accuracy: **51.64%**

---

## 🔌 API Reference

### 📍 POST `/search`

#### Request
```json
{
  "query": "copyright infringement of digital content",
  "cosine": true,
  "bayes": true
}
```

#### Response
```json
{
  "query": "...",
  "predicted_outcome": "cited",
  "confidence": 54.4,
  "similar_cases": [...]
}
```

---

### 📍 GET `/health`

```json
{
  "status": "running"
}
```

---

## ⚙️ Installation & Setup

### 📋 Requirements

| Tool | Version |
|------|--------|
| Python | 3.9+ |
| Node.js | 20+ |
| pip | Latest |
| npm | Latest |

---

### 🔧 Backend Setup

```bash
cd legal_case_finder/backend

pip3 install flask flask-cors scikit-learn pandas nltk

python3 app.py
```

---

### 🌐 Frontend Setup

```bash
cd legal_case_finder/frontend

npm install express

node app.js
```

---

### 🌍 Run Application

```
http://localhost:3000
```

---

## 🖥️ Usage

1. Open browser  
2. Enter legal query  
3. Select model(s):
   - Cosine Similarity
   - Naive Bayes  
4. Click **Search Cases**  
5. View results  

---

## ⚖️ Model Comparison

| Feature | Cosine Similarity | Naive Bayes |
|--------|------------------|------------|
| Type | Unsupervised | Supervised |
| Output | Similar cases | Predicted outcome |
| Training | Not required | Required |
| Speed | Fast | Fast |
| Best Use | Case retrieval | Outcome prediction |

---

## ⚠️ Limitations

- Moderate accuracy (~51%)
- No semantic understanding (TF-IDF limitation)
- No pagination
- HTML encoding issues (`&amp;`)

---

## 🚀 Future Improvements

- Integrate **BERT / Word2Vec**
- Add **Logistic Regression**
- Pagination support
- Advanced filtering (year, court)
- Cloud deployment

---

## 📖 Glossary

| Term | Definition |
|------|----------|
| TF-IDF | Text importance scoring |
| Cosine Similarity | Vector similarity metric |
| Naive Bayes | Probabilistic classifier |
| Stopwords | Common words removed |
| Vector Space Model | Text → numeric vectors |
| Flask | Python backend framework |
| Express | Node.js frontend server |
| REST API | HTTP communication interface |

---

## 🏁 Conclusion

This project demonstrates a **complete NLP pipeline**, combining:

- Text preprocessing
- Feature engineering
- Machine learning
- Full-stack deployment

---

## 🛠️ Tech Stack

- Python
- Flask
- scikit-learn
- NLTK
- Node.js
- Express

---

## 📌 Author Note

> Developed as an **NLP Mini Project** to showcase real-world legal text analysis and machine learning integration.
