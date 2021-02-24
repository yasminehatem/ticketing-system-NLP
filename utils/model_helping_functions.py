# -*- coding: utf-8 -*-
import xgboost as xgb
import processing_helping_functions as phf
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, accuracy_score, classification_report, precision_recall_curve
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
def predict(mytest,vectorizer,tfidfconverter,model):
    mytest,_=phf.cleaning(mytest)
    mytest=phf.Lem_stopwords(mytest)
  
    x_mytest= vectorizer.transform(mytest).toarray()
   
    x_mytest = tfidfconverter.transform(x_mytest).toarray()
    return model.predict(x_mytest)
def evaluate_models(Y_train, Y_test, train_pred, test_pred):
    print("Accuracy on Training set",accuracy_score(Y_train, train_pred))
    print("Accuracy on Testing set",accuracy_score(Y_test, test_pred))
    print(confusion_matrix(Y_test, test_pred))
    print(classification_report(Y_test, test_pred))
    


