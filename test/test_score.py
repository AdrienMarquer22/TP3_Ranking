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
        self.assertEqual(linear_function(querry,doc,index),4)
        querry =["la","karine"]
        self.assertEqual(linear_function(querry,doc,index),3)
        querry =["zer","la","karine"]
        self.assertEqual(linear_function(querry,doc,index),2)
        querry =["karine","wikipédia","karine","ok","ok"]
        self.assertEqual(linear_function(querry,doc,index),10)
        doc=2
        querry =["ok","ok"]
        self.assertEqual(linear_function(querry,doc,index),7)


    def test_linear_bm25(self):
        querry =["ok","ok"]
        doc =2
        avg_doc_len = 5.2
        doc_len = 5
        N=4
        self.assertAlmostEqual(bm25(doc,querry,index,avg_doc_len,doc_len,N) , 1.704866366424662 ) 
        save_score= bm25(doc,querry,index,avg_doc_len,doc_len,N)

        doc_len = 78
        self.assertLess(bm25(doc,querry,index,avg_doc_len,doc_len,N) , save_score ) 
        save_score= bm25(doc,querry,index,avg_doc_len,doc_len,N)
        
        avg_doc_len = 52
        doc_len = 5
        self.assertGreater(bm25(doc,querry,index,avg_doc_len,doc_len,N) ,save_score ) 
        save_score= bm25(doc,querry,index,avg_doc_len,doc_len,N)

        N=400
        self.assertGreater(bm25(doc,querry,index,avg_doc_len,doc_len,N) , save_score )
        save_score= bm25(doc,querry,index,avg_doc_len,doc_len,N)

        querry =["ok","kqrine",'888']
        self.assertLess(bm25(doc,querry,index,avg_doc_len,doc_len,N) , save_score)