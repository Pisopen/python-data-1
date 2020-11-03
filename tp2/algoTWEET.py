import pandas as pd
import sklearn
import joblib 
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from stop_words import get_stop_words
from sklearn.multiclass import OneVsRestClassifier

# TP2 DATASET TWEET
labelData = pd.read_csv("labels.csv",sep=',',encoding='iso-8859-1')
labelData = labelData.drop("Unnamed: 0",1)


clf = make_pipeline(
  TfidfVectorizer(stop_words=get_stop_words('en')),
  OneVsRestClassifier(SVC(kernel='linear', probability=True))
)

clf = clf.fit(X=labelData['tweet'], y=labelData['class'])


joblib.dump(clf, 'model.pkl')



