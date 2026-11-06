from transformers import pipeline

# 1. Initialize the native token classification pipeline
pipe = pipeline("token-classification", model="oliverguhr/fullstop-punctuation-multilang-large")

def restore_punctuation(text: str) -> str:
    # Get raw predictions from the pipeline
    predictions = pipe(text)
    
    # Track position and step through the text string word by word
    words = text.split()
    output_text = []
    
    for i, word in enumerate(words):
        # Capitalize the first word or words following sentence-ending punctuation
        if i == 0 or (output_text and output_text[-1][-1] in ['.', '?', '!']):
            word = word.capitalize()
            
        # Find if this word has an associated punctuation entity tag predicted
        # We search matching locations within the pipeline token list
        match = [p for p in predictions if word.lower() in p['word'].lower()]
        
        if match:
            # Grab the strongest entity label prediction (e.g., '0', '.', ',', '?')
            label = match[0]['entity']
            if label != '0':  # '0' means no punctuation
                word += label
                
        output_text.append(word)
        
    return " ".join(output_text)

# --- Test execution ---
raw_text = "hallo welt wie geht es dir heute ich hoffe das script funktioniert jetzt"
clean_result = restore_punctuation(raw_text)

print("Original text: ", raw_text)
print("Cleaned text:  ", clean_result)
