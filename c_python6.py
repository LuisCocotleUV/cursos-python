### 0 ###
a = ""
length = len(a)
q0.a.check()


b = "it's ok"
length = len(b)
q0.b.check()


c = 'it\'s ok'
length = len(c)
q0.c.check()


d = """hey"""
length = len(d)
q0.d.check()


e = '\n'
length = len(e)
q0.e.check()


### 1 ###
def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    if len(zip_code)==5:
        if str.isdigit(zip_code):
            return True
        else:
            return False
    else:
        return False
    pass

q1.check()


### 2 ###
def word_search(documents, keyword):
    indices = [] 
    for i, doc in enumerate(documents):
        tokens = doc.split()
        normalized = [token.rstrip('.,').lower() for token in tokens]

        if keyword.lower() in normalized:
            indices.append(i)
    return indices

q2.check()


### 3 ###
def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    my_return_dict = {}
    for i in range(len(keywords)):
        my_return_dict[keywords[i]] = word_search(doc_list,keywords[i])
    return my_return_dict
    pass

q3.check()