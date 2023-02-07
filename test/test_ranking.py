import unittest
import json
import os
from ranking.utils import token_clean
import numpy as np
from ranking.score import linear_function,bm25
from ranking.ranking import Ranking

class TestRanking(unittest.TestCase):
    def setUp(self):
        self.ranking = Ranking("karine wikipédia", method="linear")
        self.ranking_or = Ranking("karine wikipédia",type='or', method="linear")
        self.ranking.load_index(path="data/index.json")
        self.ranking.load_documents(path="data/documents.json")
        self.ranking_or.load_index(path="data/index.json")
        self.ranking_or.load_documents(path="data/documents.json")


    def test_load_index(self):
        self.assertIsNotNone(self.ranking.index)
        self.assertEqual(self.ranking.index['karine']['0']["count"],1)

    def test_load_documents(self):
        self.assertIsNotNone(self.ranking.documents)
        self.assertEqual(self.ranking.documents[0]["id"],0)

    def test_list_docs_contains_token(self):
        self.ranking.list_docs_contains_token()
        self.assertIsNotNone(self.ranking.list_docs)
        self.assertIn(self.ranking.index['karine'],self.ranking.list_docs)

        self.ranking_or.list_docs_contains_token()
        self.assertIsNotNone(self.ranking_or.list_docs)
        self.assertIn(self.ranking_or.index['wikipédia'],self.ranking.list_docs)

    def test_filter(self):
        self.ranking.filter()
        self.assertIsNotNone(self.ranking.keys)
        self.assertIn('0',self.ranking.keys)

        self.ranking_or.filter()
        self.assertIsNotNone(self.ranking_or.keys)
        self.assertIn('498',self.ranking_or.keys)

    def test_create_ranking(self):
        self.ranking.create_ranking()
        self.assertIsNotNone(self.ranking.ranking)
        self.assertEqual(6,self.ranking.ranking['0'])

        self.ranking_or.create_ranking()
        self.assertIsNotNone(self.ranking_or.ranking)
        self.assertEqual(2,self.ranking_or.ranking['498'])


    def test_result(self):
        self.ranking.create_ranking()
        self.ranking.result()
        self.assertIsNotNone(self.ranking.res)
        self.assertEqual('Karine Lacombe \u2014 Wikip\u00e9dia',self.ranking.res['0']['title'])
        self.assertEqual('https://fr.wikipedia.org/wiki/Karine_Lacombe',self.ranking.res['0']['url'])

    def test_save_result(self):
        self.ranking.create_ranking()
        self.ranking.result()
        self.ranking.save_result("test/result.json")
        self.assertTrue(os.path.exists("test/result.json"))

