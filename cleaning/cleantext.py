import string
import re

def clean_text(text):
     # Lowercase all text
     text = text.lower()
     # Remove punctuation
     text = text.translate(str.maketrans('', '', string.punctuation))
     # Remove numbers
     text = re.sub(r'\d+', '', text)
     # Split into words
     words = text.split()
     # Optionally: filter out very short words (like single letters)
     words = [word for word in words if len(word) > 1]
     # Join words back into cleaned text
     return ' '.join(words)
 
with open('input.txt', 'r', encoding='utf-8') as f:
     raw_text = f.read()
 
cleaned_text = clean_text(raw_text)
 
with open('cleaned.txt', 'w', encoding='utf-8') as f:
     f.write(cleaned_text)
