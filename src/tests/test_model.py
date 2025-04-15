import unittest
from src.model import load_sentiment_model, predict_sentiment

class TestSentimentModel(unittest.TestCase):
    def test_model_loading(self):
        tokenizer, model = load_sentiment_model()
        self.assertIsNotNone(tokenizer)
        self.assertIsNotNone(model)

    def test_sentiment_prediction(self):
        tokenizer, model = load_sentiment_model()
        texts = ["I love this!", "This is terrible."]
        sentiments = predict_sentiment(texts, tokenizer, model)
        self.assertEqual(len(sentiments), 2)
        self.assertEqual(sentiments[0], 'positive')
        self.assertEqual(sentiments[1], 'negative')

if __name__ == '__main__':
    unittest.main()