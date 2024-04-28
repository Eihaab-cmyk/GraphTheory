import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re

#nltk.download('punkt')
#nltk.download('stopwords')

# Tokenization, stop-word removal, and stemming function
def preprocess_text(text):
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words]
    
    # Initialize stemmer
    stemmer = PorterStemmer()
    
    # Stemming
    stemmed_words = [stemmer.stem(word) for word in words]
    
    # Join the stemmed words back into a single string
    preprocessed_text = ' '.join(stemmed_words)
    
    return preprocessed_text


file_path = "Scrapped_data/Marketing_test/Marketing_test_3_data.txt"  # Path to data file
output_file_path = "preprocessed_Marketing_3_test_data.txt"  # Path to save preprocessed data

with open(file_path, "r", encoding="utf-8") as file:
    data = file.read()

preprocessed_data = preprocess_text(data)

with open(output_file_path, "w", encoding="utf-8") as file:
    file.write(preprocessed_data)

print("Preprocessing complete and saved to:", output_file_path)