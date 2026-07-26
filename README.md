#  SMS Spam Classifier

A Machine Learning-based web application that classifies SMS or Email messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP). The application is built with **Python**, **Scikit-learn**, and **Streamlit**.

## Features

- Detects Spam and Ham messages
- Interactive web interface using Streamlit
- Text preprocessing with NLTK
- TF-IDF Vectorization
- Trained and compared multiple Machine Learning models
- Fast and easy to use

## Dataset

The model was trained on the **SMS Spam Collection Dataset**, containing labeled SMS messages categorized as Spam or Ham.

## Workflow

1. Data Cleaning
   - Removed duplicate entries
   - Handled missing values

2. Text Preprocessing
   - Converted text to lowercase
   - Tokenization using NLTK
   - Removed punctuation and special characters
   - Removed stopwords
   - Applied stemming

3. Feature Engineering
   - Text transformation using **TF-IDF Vectorizer** from Scikit-learn

4. Model Training
   The following algorithms were trained and evaluated:
   - Multinomial Naive Bayes (MNB)
   - Bernoulli Naive Bayes (BNB)
   - Extra Trees Classifier (ETC)
   - XGBoost Classifier

5. Model Selection
   Among all the trained models, **Extra Trees Classifier (ETC)** achieved the best performance and was selected as the final model for deployment.

## Technologies Used

- Python
- Streamlit
- Scikit-learn
- NLTK
- Pandas
- NumPy
- XGBoost

## Project Structure

```
spam-classifier/
│── app.py
│── model.pkl
│── vectorizer.pkl
│── requirements.txt
│── README.md
```

## How to Run

1. Clone the repository

```bash
git clone https://github.com/veer714/spam-classifier.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the application

```bash
streamlit run app.py
```

## Future Improvements

- Email attachment analysis
- Confidence score visualization
- Multi-language spam detection
- Deep Learning models (LSTM/BERT)

## Author

**Veer Pratap**

B.Tech (AI & Data Science)
