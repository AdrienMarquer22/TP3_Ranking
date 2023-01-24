
import re

def token_clean(string):
    return re.sub(r'[^\w\s]', '', string.lower()).split()