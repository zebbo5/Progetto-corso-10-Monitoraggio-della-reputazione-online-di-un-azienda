from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

def load_sentiment_model(model_name="cardiffnlp/twitter-roberta-base-sentiment-latest"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return tokenizer, model

def predict_sentiment(texts, tokenizer, model):
    encoded_input = tokenizer(texts, padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        output = model(**encoded_input)
    probabilities = torch.nn.functional.softmax(output.logits, dim=-1)
    predicted_labels = torch.argmax(probabilities, dim=-1)
    labels = ['negative', 'neutral', 'positive']
    predicted_sentiments = [labels[label] for label in predicted_labels.tolist()]
    return predicted_sentiments

if __name__ == "__main__":
    tokenizer, model = load_sentiment_model()
    texts = ["This is great!", "I'm so sad.", "The weather is okay."]
    sentiments = predict_sentiment(texts, tokenizer, model)
    for text, sentiment in zip(texts, sentiments):
        print(f"Text: '{text}' - Sentiment: {sentiment}")