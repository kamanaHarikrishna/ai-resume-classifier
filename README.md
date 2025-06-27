# 🧠 AI Resume Category Classifier

This project is an **AI-powered web application** that classifies resumes into predefined job categories using **Natural Language Processing (NLP)** and **Machine Learning (ML)** models. It’s built with **Streamlit** for a clean and interactive UI.

---

## 🎯 Objective

Automatically categorize candidate resumes (e.g., Data Scientist, HR, Developer, Designer) based on content — reducing manual sorting time for recruiters and improving hiring workflows.

---

## 🧰 Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **ML Model**: Multinomial Naive Bayes  
- **Vectorization**: TF-IDF (Term Frequency-Inverse Document Frequency)  
- **Libraries**:  
  - scikit-learn  
  - pandas  
  - numpy  
  - nltk  
  - joblib  
  - re  
  - PIL / base64 (for styling)

---

## 🖼️ Demo Features

- Paste resume content into the text area
- One-click prediction of resume category
- Custom background styling
- Clean and responsive UI

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/kamanaHarikrishna/ai-resume-classifier.git
cd ai-resume-classifier
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
ai-resume-classifier/
│
├── app.py                    # Streamlit application
├── resume_classifier.pkl     # Trained ML model
├── TfidfVectorizer.pkl       # Fitted TF-IDF vectorizer
├── requirements.txt          # Python dependencies
├── background.png            # Background image (optional)
└── UpdatedResumeDataSet.csv  # Dataset used (optional for retraining)
```

---

## ⚙️ Model Training (Optional)

If you want to retrain the model:

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Preprocess and clean your dataset...
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(cleaned_resume_texts)
model = MultinomialNB()
model.fit(X, labels)

# Save artifacts
joblib.dump(model, 'resume_classifier.pkl')
joblib.dump(vectorizer, 'TfidfVectorizer.pkl')
```

---

## 📊 Categories Supported

- Data Science  
- HR  
- Developer  
- Designer  
- Web Developer  
- Python Developer  
- Business Analyst  
- ... (Based on training data)

---

## 📸 UI Preview

> Add screenshots or GIFs here for better visual understanding.

---

## 👨‍💻 Author

**Hari Krishna Kamana**  
🔗 [LinkedIn](https://www.linkedin.com/in/kamanaharikrishna)

---

## 📄 License

This project is licensed under the MIT License.

