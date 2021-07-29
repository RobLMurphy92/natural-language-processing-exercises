from requests import get
from bs4 import BeautifulSoup
import os
import requests
import pandas as pd

import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd
import acquire

import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd



def basic_clean(article):
    '''
    This function will take any text corpus and lower case everything and 
    remove any accented characters, non-ASCII characters. Will do this through encode which converts to ascii,
    then decode which will turn the bytes object back into a string.
    '''
    #lower casing everything for normalicy
    article = article.lower()
    #ridding of non-ascii characters by conversion, then changing the bytes object backinto string.
    article = unicodedata.normalize('NFKD', article).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    
    return article




def tokenize_func(article):
    '''
    function will tokenize the string, essentially break words and any punctuation left over into discrete units.
    '''
    tokenizer = nltk.tokenize.ToktokTokenizer()
    article = tokenizer.tokenize(article, return_str=True)
    
    return article


def stem(article):
    '''
    takes in string and will stem transformation to all words within the specifiec string
    '''
    ps = nltk.porter.PorterStemmer()
    
    stems = [ps.stem(word) for word in article.split()]
    
    article_stemmed = ' '.join(stems)
    return article_stemmed


    #lexicographically correct word (present in the dictionary),
def lemmatize(article):
    '''
     this function takes in a string and utilize lemmatization on the string
     which change word to root word which will  be lexicographically correct word (present in the dictionary).
    '''
    wnl = nltk.stem.WordNetLemmatizer()
    for word in article.split():
        lemmas = [wnl.lemmatize(word) for word in article.split()]
        article_lemmatized = ' '.join(lemmas)
    return article_lemmatized

def remove_stopwords(string, extra_words =[], exclude_words =[]):
    stopword_list = stopwords.words('english')
    #removing exclude words, from stopword list
    stopword_list = set(stopword_list) - set(exclude_words)
    
    #add extra words
    stopword_list = stopword_list.union(set(extra_words))
    
    words = string.split()
    filtered_words = [w for w in words if w not in stopword_list]
    string_without_stopwords = ' '.join(filtered_words)
    
    return string_without_stopwords