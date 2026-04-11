# Myers-Briggs Personality Type Predictor (MBTI)

![MBTI Banner](https://images.unsplash.com/photo-1506126613408-eca07ce68773?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80)

## 📌 Overview
This project is an end-to-end Machine Learning web application that predicts a user's **Myers-Briggs Type Indicator (MBTI)** personality based on text samples. Using advanced Natural Language Processing (NLP) and ensemble learning models, the application analyzes writing styles to classify users into one of the 16 unique MBTI personality types.

The MBTI assessment is a psychometric tool designed to measure psychological preferences in how people perceive the world and make decisions across four dimensions:
- **Introversion (I) vs. Extraversion (E)**
- **Intuition (N) vs. Sensing (S)**
- **Thinking (T) vs. Feeling (F)**
- **Judging (J) vs. Perceiving (P)**

---

## 🚀 Key Features
- **Real-time Prediction:** Input text snippets and get instant personality type results.
- **Multidimensional Analysis:** Independent models for each of the four MBTI dimensions to ensure higher accuracy.
- **Data Preprocessing:** Robust cleaning pipeline (lemmatization, stopword removal, regex-based URL/handle cleaning).
- **Comprehensive Visualizations:** In-depth data analysis and model performance metrics included in the Exploratory Data Analysis (EDA) phase.
- **Dockerized Deployment:** Easy to deploy and scale using Docker and Docker Compose.

---

## 🛠️ Technology Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML5, CSS3, Bootstrap 4
- **Machine Learning:** Scikit-learn, XGBoost, CatBoost
- **NLP:** NLTK (Natural Language Toolkit), TF-IDF Vectorization
- **Data Processing:** Pandas, NumPy
- **Containerization:** Docker, Docker Compose
- **Environment:** Python 3.9+

---

## 📂 Project Structure
```bash
College_Project/
├── app.py                  # Flask application entry point
├── Datasets/               # Training data (MBTI Kaggle dataset)
├── artifacts/              # Pretrained models & vectorizers (.pkl)
├── src/                    # Source code & logic
│   ├── utils.py            # Utility functions for cleaning & persistence
│   └── *.ipynb             # Jupyter Notebooks for EDA & Training
├── static/                 # CSS, JS, and image assets
├── templates/              # HTML frontend templates
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose configuration
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/NagothuSuryaTeja/Final-Year-Project.git
cd Final-Year-Project
```

### 2️⃣ Manual Setup (Local Environment)
1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   python app.py
   ```
4. **Access the app:** Open `http://127.0.0.1:5000` in your browser.

### 3️⃣ Setup with Docker 🐳
If you have Docker installed, you can run the application with a single command:
```bash
docker-compose up --build
```
The app will be available at `http://localhost:5000`.

---

## 🧠 Model Pipeline
The project follows a rigorous data science workflow:
1. **Data Collection:** Utilizing the MBTI 6k+ posts dataset from Kaggle.
2. **Preprocessing:** Advanced cleaning techniques including URL removal, lemmatization, and handling imbalanced datasets.
3. **Feature Engineering:** TF-IDF (Term Frequency-Inverse Document Frequency) to convert text into numerical vectors.
4. **Model Selection:** Comparison of multiple algorithms (Logistic Regression, Random Forest, XGBoost, CatBoost).
5. **Hyperparameter Tuning:** Optimized using GridSearchCV to find the best performing parameters.
6. **Inference:** A separate classifier is trained for each of the 4 MBTI dimensions, and results are combined for final output.

---

## 📊 Evaluation Metrics
The models are evaluated based on:
- **Accuracy Score**
- **F1-Score** (Crucial for imbalanced classes)
- **Confusion Matrix**

---

## 🤝 Contributing
Contributions are welcome! If you have suggestions for improvement, please open an issue or submit a pull request.

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Developed by [Surya Teja](https://github.com/NagothuSuryaTeja)**