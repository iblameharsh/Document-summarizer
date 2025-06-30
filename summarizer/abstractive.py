from transformers import BartTokenizer, BartForConditionalGeneration

# Load tokenizer and model
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

def abstractive_summary(text, min_length=100, max_length=200):
    # Tokenize input
    inputs = tokenizer.encode(text, return_tensors="pt", max_length=1024, truncation=True)

    # Generate summary
    summary_ids = model.generate(
        inputs,
        min_length=min_length,
        max_length=max_length,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True
    )

    # Decode summary
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)
