import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')


text = "Hello! I am a member of Advait Club."


text_lower = text.lower()


text_clean = text_lower.translate(str.maketrans('', '', string.punctuation))

words = word_tokenize(text_clean)


stop_words = set(stopwords.words('english'))
final_words = []

for word in words:
    if word not in stop_words:
        final_words.append(word)


print("Original:", text)
print("Cleaned:", text_clean)
print("Tokens:", words)
print("After Stopword Removal:", final_words)
