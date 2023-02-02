import numpy as np
import nltk
from nltk.corpus import stopwords
import math
nltk.download('stopwords')
stop_words = set(stopwords.words('french'))

def linear_function(query,doc,index):
    """
    Parameters:
        query (list of str): The query to score against.
        doc (int): The document to score.
        index (dict of dict): The index
    Returns:
        float: The score.
    """
    score = 0
    distance = 0
    i=0
    for token in query:
        if doc in index[token]:
            # count weight
            score += index[token][doc]["count"] - 1
            ##distance
            distance += np.min([abs(i-x) for x in index[token][doc]["positions"]])
            i+=1
            ##stopword
            if token not in stop_words:
                score += 2
            else:
                score -= 4 # we remove weight because the word isnt in the docs
            score -= distance
    return score



def bm25(doc, query, index,avg_doc_len,k1=1.2, b=0.75):
    """
    Parameters:
        query (list of str): The query to score against.
        doc (int): The document to score.
        index (dict of dict): The index
        avg_doc_len (float): The average len of document
        k1 (float, optional): The k1 parameter, defaults to 1.2.
        b (float, optional): The b parameter, defaults to 0.75.       
    Returns:
        float: The BM25 score.
    """
    # Create a dictionary of the words and their frequencies in the document + length of the document
    doc_word_freq = {}
    len_doc = 0
    for word in index:
        if doc in  index[word]:
            doc_word_freq[word] = index[word][doc]["count"]
            len_doc += index[word][doc]["count"]
            

    # Calculate the average document

   
    # Compute the BM25 score for each word in the query.
    score = 0
    for word in query:
        if word not in doc_word_freq:
            continue
        freq = doc_word_freq[word]
        idf = math.log((len_doc - freq + 0.5) / (freq + 0.5))
        score += idf * (freq * (k1 + 1) / (freq + k1 * (1 - b + b * len_doc / avg_doc_len)))
   
    return score