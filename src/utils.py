    ## Data Cleaning - IMP
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pickle
import os
nltk.download('wordnet')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
class DataCleaning:
    def __init__(self):
        pass
    
    def clean_text_advanced(self,text):
        text = text.lower()

        text = re.sub(r"http\S+|www\S+|https\S+", '', text)

        text = re.sub(r'@\w+', '', text)

        text = re.sub(r'\d+', '', text)

        text = text.translate(str.maketrans('', '', string.punctuation))

        tokens = text.split()

        tokens = [word for word in tokens if word not in stop_words and len(word) > 2]

        tokens = [lemmatizer.lemmatize(word) for word in tokens]

        cleaned_text = ' '.join(tokens)

        return cleaned_text
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        print(e)
    
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        print(e)