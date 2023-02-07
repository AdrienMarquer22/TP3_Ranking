# Adrien MARQUER - TP3 Ranking


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt
```

## Usage

Launch with the command 
```bash
python3 main.py 
    [--request request]
    [--type type]
    [--linear]
    [--bm25]
    [--name name]
```

There is 5 arguments to use :
+ `request` : The querry that you want to execute
+ `type` : The type of filtering `And` or `Or` (default = `And`)
+ `linear` : Score with the linear function (default = `False`)
+ `bm25` : Score with the BM25 function (default = `False`)
+ `name` : The name for the result json file (default = `result`)



```bash
# Launch the tests 
python3 -m unittest discover test/

python3 main.py --request "Karine Lacombe" --type And --linear

python3 main.py --request "Karine Lacombe Wikipédia" --type or --bm25 --name BM25

python3 main.py --request "Wikipédia Chicago" --type or --name Wikipedia --bm25 --linear



```


## File

### Ranking (`rankink.py`)

A class for ranking documents based on the input request.

 #### Requirements
+ [numpy](https://numpy.org/)

#### Usage

```python
from ranking import Ranking

# Create an instance of the Ranking class
r = Ranking("sample request", type="And", method="linear")

# Load the index and document data
r.load_index()
r.load_documents()

# Create the ranking
r.create_ranking()

# Get the result
r.result()

# Save the result to a file
r.save_result("result.json")
```

#### Parameters

+ `request`: The string to be used for ranking the documents.
+ `type` (optional): The type of filtering (if you want all the token in the document or at least 1), either `And` or `Or`. Default is `And`.
+ `method` (optional): The method used for ranking the documents, either `linear` or `bm25`. Default is `linear`.

#### Methods
+ `load_index`: Load the index data from a json file (default: `data/index.json`).
+ `load_documents`: Load the document data from a json file (default: `data/documents.json`).
+ `create_ranking`: Create the ranking of documents based on the input request and the specified type and method.
+ `result`: Get the resulting ranked documents.
+ `save_resul`t: Save the resulting ranked documents to a json file.


### Score (`score.py`)

This repository contains two functions for scoring a document against a query: `linear_function` and `bm25`.

#### Requirements
+ [numpy](https://numpy.org/)
+ [nltk](https://www.nltk.org/)


#### Usage
+ Download the nltk stopwords corpus by running `nltk.download('stopwords')`.
+ Import the functions by adding `from document_scoring import linear_function, bm25` to your code.
+ The functions take the following parameters:
  + `query` (list of str): The query to score against.
  + `doc` (int): The document to score.
  + `index` (dict of dict): The index.
  + `avg_doc_len` (float) (only for `bm25` function): The average length of documents.
  + `doc_len` (float) (only for `bm25` function): The length of the document.
  + `N` (int) (only for `bm25` function): Total number of documents.
  + `k1` (float, optional) (only for `bm25` function): The k1 parameter, defaults to 1.2.
  + `b` (float, optional) (only for `bm25` function): The b parameter, defaults to 0.75.
+ The functions return a float, representing the score of the document against the query.

#### Function Details
+ `linear_function`: A basic linear scoring function that takes into account the frequency and position of query words in the document, as well as whether the query words are stop words.
+ `bm25`: An implementation of the BM25 scoring function, which is widely used in information retrieval. BM25 is a probabilistic model that scores documents based on the relevance of the query terms in the document and the importance of the terms in the collection.


Note: The code is provided in French, with the stop words set to the French language. If you need it in a different language, you will need to change the `stop_words` variable accordingly.
