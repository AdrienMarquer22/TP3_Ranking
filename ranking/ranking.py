import json
from ranking.utils import token_clean
import numpy as np
import nltk
from nltk.corpus import stopwords

class Ranking():
    def __init__(self,request,type="And") -> None:
        self.index=[]
        self.request=request
        self.request_token = token_clean(request)
        self.list_docs=[]
        self.ranking=[]
        self.type=type.lower()
        self.documents = []

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
        nltk.download('stopwords')
        stop_words = set(stopwords.words('french'))

        self.filter()
        self.ranking={}
        for doc in self.keys:
            i=0
            distance = 0
            for token in self.request_token:
                if doc in self.index[token]:
                    self.ranking.setdefault(doc , 0)
                    self.ranking[doc] += self.index[token][doc]["count"]

                    ##distance
                    distance += np.min([abs(i-x) for x in self.index[token][doc]["positions"]])
                    i+=1

                    ##stopword
                    if token not in stop_words:
                        self.ranking[doc] += 2

                else:
                    self.ranking.setdefault(doc , 0)
                    self.ranking[doc] -= 4 # we remove weight because the word isnt in the docs


            self.ranking[doc] -= distance
            self.ranking[doc] -= len(self.list_docs) #we remove the number of token to make sure the counn weight dosnt increase with the nmber of words
        self.ranking = {k: v for k, v in sorted(self.ranking.items(), key=lambda item: item[1], reverse=True)}

    def result(self):
        self.res={}
        for doc in self.ranking:
            docu = [d for d in self.documents if d['id']  == int(doc)]
            self.res[doc] = {"title": docu[0]["title"],"url":docu[0]["url"]}

    def save_result(self,name):
        with open(name, 'w') as outfile:
            json.dump(self.res, outfile, ensure_ascii=False,indent=4) 
            

        

