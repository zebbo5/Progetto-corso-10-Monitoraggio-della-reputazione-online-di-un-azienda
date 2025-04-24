from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Funzione per caricare il tokenizer e il modello pre-addestrato per l'analisi del sentiment
def load_sentiment_model(model_name="cardiffnlp/twitter-roberta-base-sentiment-latest"):
    # Carica il tokenizer associato al modello specificato
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    # Carica il modello per la classificazione di sequenze (sentiment analysis)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    # Restituisce sia il tokenizer che il modello
    return tokenizer, model

# Funzione per prevedere il sentiment di una o più stringhe di testo
def predict_sentiment(texts, tokenizer, model):
    # Codifica il testo/i testi utilizzando il tokenizer.
    encoded_input = tokenizer(texts, padding=True, truncation=True, return_tensors='pt')

    # Disabilita il calcolo dei gradienti
    with torch.no_grad():
        # Passa gli input codificati al modello per ottenere gli output (logits).
        output = model(**encoded_input)

    # Applica la funzione softmax ai logits per ottenere le probabilità per ciascuna classe (negativo, neutro, positivo).
    probabilities = torch.nn.functional.softmax(output.logits, dim=-1)

    # Trova l'indice della classe con la probabilità più alta per ogni testo.
    predicted_labels = torch.argmax(probabilities, dim=-1)

    # Definisce le etichette corrispondenti agli indici delle classi.
    labels = ['negative', 'neutral', 'positive']

    # Mappa gli indici delle etichette predette alle stringhe di sentiment corrispondenti.
    # Converti il tensore PyTorch in una lista Python con .tolist().
    predicted_sentiments = [labels[label] for label in predicted_labels.tolist()]

    # Restituisce la lista dei sentimenti predetti per ogni testo.
    return predicted_sentiments

# Blocco principale che viene eseguito solo quando lo script viene eseguito direttamente
if __name__ == "__main__":
    # Carica il tokenizer e il modello predefiniti.
    tokenizer, model = load_sentiment_model()

    # Definisce una lista di testi di esempio per l'analisi.
    texts = ["This is great!", "I'm so sad.", "The weather is okay."]

    # Esegue la predizione del sentiment sui testi di esempio.
    sentiments = predict_sentiment(texts, tokenizer, model)

    # Itera sui testi e i sentimenti predetti e li stampa.
    for text, sentiment in zip(texts, sentiments):
        print(f"Text: '{text}' - Sentiment: {sentiment}")
