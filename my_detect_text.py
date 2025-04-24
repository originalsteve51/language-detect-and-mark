import re
from langdetect import detect, DetectorFactory
# Ensures consistent results across multiple runs
DetectorFactory.seed = 0

def is_english(text):
    """Detect if a given text is in English."""
    try:
        return detect(text) == 'en'
    except Exception as e:
        print(f"Error detecting language for text '{text}': {e}")
        return False

def extract_non_english_phrases(text):
    """Extract non-English phrases from the provided text."""
    # Consider phrases separated by punctuation or newlines
    phrases = re.split(r'[\s\n,.!?;:]+', text)
    non_english_phrases = []
    english_phrases = []
    for phrase in phrases:
        if phrase and not is_english(phrase):
            non_english_phrases.append(phrase)
        else:
            english_phrases.append(phrase)
    return non_english_phrases, english_phrases

def main():
    # Load your text document
    filepath = './sample1.txt'  # Change to your document path
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
    non_english_phrases, english_phrases = extract_non_english_phrases(text)
    
    print("Non-English Phrases Found:")
    for phrase in non_english_phrases:
        print(phrase)
    print("English Phrases Found:")
    for phrase in english_phrases:
        print(phrase)
    
if __name__ == "__main__":
    main()