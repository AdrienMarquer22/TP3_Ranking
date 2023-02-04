import json
from ranking.utils import token_clean
import numpy as np

from ranking.score import linear_function,bm25

class Ranking():
    def __init__(self,request,type="And",method='linear') -> None:
        self.index=[]
        self.request=request
        self.request_token = token_clean(request)
        self.list_docs=[]
        self.ranking=[]
        self.type=type.lower()
        self.documents = []
        self.method = method

    def load_index(self,path="data/index.json"):
        self.index = json.load(open(path))

    def load_documents(self,path="data/documents.json"):
        self.documents = json.load(open(path))

    def list_docs_contains_token(self):
        for token in self.request_token:
            if token in self.index:
                self.list_docs.append(self.index[token])


    def filter(self):
        self.list_docs_contains_token()
        if self.type == 'and':
            self.keys = set(self.list_docs[0].keys())
            if len(self.list_docs) > 1 :
                for d in self.list_docs[1:]:
                    self.keys.intersection_update(d.keys())
        elif self.type == 'or':
            self.keys = set(self.list_docs[0].keys())
            if len(self.list_docs) > 1 :
                for d in self.list_docs[1:]:
                    self.keys = self.keys.union(d.keys())
        else:
            raise Exception("Incorect type try 'Or' or 'And'")

    def create_ranking(self):
        self.filter()
        self.ranking={}
        self.avg_len_loc = np.mean([len(docu['title'].split()) for docu in self.documents])
        N=len(self.documents)
        for doc in self.keys:
            if self.method.lower() == 'linear':
                self.ranking[doc] = linear_function(self.request_token,doc,self.index) #we remove the number of token to make sure the counn weight dosnt increase with the nmber of words
            elif self.method.lower() == 'bm25':

                doc_len = self.longueur_doc(int(doc))
                self.ranking[doc]=bm25(doc,self.request_token,self.index,self.avg_len_loc,doc_len,N,k1=1.2, b=0.75)

        self.ranking = {k: v for k, v in sorted(self.ranking.items(), key=lambda item: item[1], reverse=True)}

    def longueur_doc(self,id:int):
        return len(next((item['title'].split() for item in self.documents if item['id'] == id), []))

    def result(self):
        self.res={}
        for doc in self.ranking:
            docu = [d for d in self.documents if d['id']  == int(doc)]
            self.res[doc] = {"title": docu[0]["title"],"url":docu[0]["url"]}

    def save_result(self,name):
        with open(name, 'w') as outfile:
            json.dump(self.res, outfile, ensure_ascii=False,indent=4) 
            

        

