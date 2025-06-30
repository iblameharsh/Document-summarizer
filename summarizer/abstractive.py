def abstractive_summary(text, min_length=100, max_length=200):
    from transformers import BartTokenizer, BartForConditionalGeneration
    tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
    model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

    chunks = [para.strip() for para in text.split('\n') if para.strip()]
    summaries = []

    for chunk in chunks:
        inputs = tokenizer.encode(chunk, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = model.generate(
            inputs,
            min_length=min_length,
            max_length=max_length,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True
        )
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        summaries.append(summary)

    return "\n".join(summaries)

