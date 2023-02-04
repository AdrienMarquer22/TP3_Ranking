from ranking.score import linear_function,bm25
index = {"karine": {1: {"count": 1, "positions": [0]},
                       2: {"count": 2, "positions": [1, 3]}},
             "wikipédia": {1: {"count": 1, "positions": [1]},
                       2: {"count": 1, "positions": [0]}},
             "ok": {2: {"count": 2, "positions": [2, 4]}}}

             
querry =["ok","ok"]
doc =2
avg_doc_len = 5.2
doc_len = 5
N=4

tt = bm25(doc,querry,index,avg_doc_len,doc_len,N)



print(tt)
