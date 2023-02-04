import unittest
from ranking.score import linear_function,bm25


index = {"karine": {1: {"count": 1, "positions": [0]},
                       2: {"count": 2, "positions": [1, 3]}},
             "wikipédia": {1: {"count": 1, "positions": [1]},
                       2: {"count": 1, "positions": [0]}},
             "ok": {2: {"count": 2, "positions": [2, 4]}}}

class TestScore(unittest.TestCase):
    def test_linear_function(self):
        doc = 1
        querry = ["karine"]
        self.assertEqual(linear_function(querry,doc,index),2)
        querry =["la","karine"]
        self.assertEqual(linear_function(querry,doc,index),1)
        querry =["zer","la","karine"]
        self.assertEqual(linear_function(querry,doc,index),0)
        querry =["karine","wikipédia","karine","ok","ok"]
        self.assertEqual(linear_function(querry,doc,index),4)
        doc=2
        querry =["ok","ok"]
        self.assertEqual(linear_function(querry,doc,index),1)


    def test_linear_bm25(self):
        querry =["ok","ok"]
        doc =2
        avg_doc_len = 5.2
        doc_len = 5
        N=4
        self.assertAlmostEqual(bm25(doc,querry,index,avg_doc_len,doc_len,N) , 1.704866366424662 ) 
        doc_len = 78
        self.assertAlmostEqual(bm25(doc,querry,index,avg_doc_len,doc_len,N) , 0.017475147188782875 ) 
        avg_doc_len = 52
        doc_len = 5
        self.assertAlmostEqual(bm25(doc,querry,index,avg_doc_len,doc_len,N) , 3.393059223153239 ) 
        N=400
        self.assertAlmostEqual(bm25(doc,querry,index,avg_doc_len,doc_len,N) , 13.643137087648006 )
        querry =["ok","kqrine",'888']
        self.assertAlmostEqual(bm25(doc,querry,index,avg_doc_len,doc_len,N) , 6.821568543824003)