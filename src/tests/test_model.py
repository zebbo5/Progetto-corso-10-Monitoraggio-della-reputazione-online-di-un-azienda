import unittest
from src.model import load_sentiment_model, predict_sentiment

# Definisce una classe di test che eredita da unittest.TestCase
# Ogni metodo che inizia con 'test_' in questa classe verrà eseguito come test unitario
class TestSentimentModel(unittest.TestCase):

    # Metodo di test per verificare il caricamento del modello e del tokenizer
    def test_model_loading(self):
        # Chiama la funzione per caricare il tokenizer e il modello
        tokenizer, model = load_sentiment_model()
        # Asserisce che il tokenizer non sia None (cioè, che sia stato caricato correttamente)
        self.assertIsNotNone(tokenizer)
        # Asserisce che il modello non sia None
        self.assertIsNotNone(model)

    # Metodo di test per verificare la predizione del sentiment
    def test_sentiment_prediction(self):
        # Carica il tokenizer e il modello (necessari per la predizione)
        tokenizer, model = load_sentiment_model()
        # Definisce una lista di testi di esempio da testare
        texts = ["I love this!", "This is terrible."]
        # Chiama la funzione predict_sentiment con i testi, tokenizer e modello
        sentiments = predict_sentiment(texts, tokenizer, model)

        # Asserisce che la lista di sentimenti restituiti abbia la stessa lunghezza della lista di input
        self.assertEqual(len(sentiments), len(texts))
        # Asserisce che il sentiment predetto per il primo testo sia 'positive'
        self.assertEqual(sentiments[0], 'positive')
        # Asserisce che il sentiment predetto per il secondo testo sia 'negative'
        self.assertEqual(sentiments[1], 'negative')

# Questo blocco viene eseguito solo se lo script viene eseguito direttamente
if __name__ == '__main__':
    # Esegue i test definiti nella classe TestSentimentModel
    unittest.main()
