import langid
import re

MAX_WORDS=1

def is_english(text):
    """Detect if a given text is in English."""
    language, confidence = langid.classify(text)
    return language == 'en' and confidence > -900.0  # Adjust the confidence threshold as needed

def split_into_sub_phrases(phrase, max_words=MAX_WORDS):
    """Split a long phrase into sub-phrases of at most max_words."""
    words = phrase.split()
    return [' '.join(words[i:i + max_words])\
                for i in range(0, len(words), max_words)]

def extract_non_english_phrases(text):
    """Extract non-English phrases from the provided text."""
    # Split the text into sentences
    sentences = re.split(r'(?<=[.!?]) +', text)  # Split by sentence endings

    non_english_phrases = []
    for sentence in sentences:
        # Check if the sentence has at least MAX_WORDS words
        word_list = sentence.split()
        if len(word_list) >= MAX_WORDS:
            if not is_english(sentence):
                # Split into sub-phrases of at most MAX_WORDS words
                sub_phrases = split_into_sub_phrases(sentence)
                finished = False
                while not finished:
                    if not is_english(sub_phrases[0]):
                        # Following used to be extend, needs to be append
                        non_english_phrases.append(sub_phrases[0])
                    if len(sub_phrases)>1:
                        sub_phrases = sub_phrases[1::]
                    else:
                        finished = True
                    

    return non_english_phrases

def main():
    # Load your text document
    filepath = './sample1.txt'  # Change to your document path
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
    non_english_phrases = extract_non_english_phrases(text)
    
    print(f"{len(non_english_phrases)} Non-English Phrases Found:")
    for phrase in non_english_phrases:
        print(phrase)

if __name__ == "__main__":
    main()