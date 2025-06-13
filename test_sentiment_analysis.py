import unittest
from SentimentAnalysis.sentiment_analysis import analyse

class TestSentimentAnalysis(unittest.TestCase):
    def test_sentiment_analyzer(self):
        result_1 = analyse("I love working with Python")
        self.assertEqual(result_1["label"], "SENT_POSITIVE")

        result_2 = analyse("I hate working with Python")
        self.assertEqual(result_2["label"], "SENT_NEGATIVE")

        result_3 = analyse("I neutral working with Python")
        self.assertEqual(result_3["label"], "SENT_NEUTRAL")

unittest.main()
