# -*- coding: utf-8 -*-
# + {}
import pandas as pd
import numpy as np
import re
import nltk
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from spacy.lang.fr.stop_words import STOP_WORDS as fr_stop
from spacy.lang.en.stop_words import STOP_WORDS as en_stop
from nltk.tokenize.treebank import TreebankWordDetokenizer as Detok
from langdetect import detect
import ipyparallel as ipp
from spacy.lang.en import English
from nltk.stem import WordNetLemmatizer
import imblearn
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle 
from collections import Counter
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, accuracy_score, classification_report, precision_recall_curve
import xgboost as xgb


#Sort out the most used keywords in "Incident-Subject" and "Ticket-Description" columns
def cleaning(my_tick):
    my_corpus=[]
    if(isinstance(my_tick, str)):
        my_corpus.append(my_tick)
    else:
        my_corpus=my_tick 
    res=[]
    drop_ind=[]
    for i in range(len(my_corpus)):
        
            
            my_corpus[i]=re.sub('[^a-zA-Z-ÖØ-öø-ÿЀ]',' ',str(my_corpus[i]))
            #lower case
            my_corpus[i]=my_corpus[i].lower()

            #remove special characters
            my_corpus[i]=re.sub("\\d|\\W"," ",str(my_corpus[i]))

            #remove tags
            if(not(str(my_corpus[i])=="" or str(my_corpus[i])=='' or str(my_corpus[i]).isspace())):
                res.append(str(re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",str(my_corpus[i]))))
            else:
                drop_ind.append(i)
        
    return res,drop_ind
def Lem_stopwords(my_tick):
    nlp_fr = spacy.load('fr_core_news_md')
    nlp_en=English()
    my_corpus=[]
    if(isinstance(my_tick[0], list)):
        my_corpus.append(my_tick[0])
    else:
        my_corpus=my_tick 
       
    for i in range (len(my_corpus)):
        li=[]
        if(detect(my_corpus[i]))=='fr':
            lists=nlp_fr(my_corpus[i])
            [li.append(str(token.lemma_)) for token in lists if not str(token.lemma_) in list(fr_stop)]
        else:
            lists=nlp_en(my_corpus[i])
            [li.append(str(token.lemma_)) for token in lists if not str(token.lemma_) in list(en_stop)]
       
        
        detokenizer = Detok()
        my_corpus[i] = detokenizer.detokenize(li)
        my_corpus[i]=re.sub(' +', ' ', my_corpus[i])
        #print(corpus[i])
    return my_corpus

#RUN TO GET THE PROCESSED LIST
# -


