import numpy as np
from os import listdir
from nltk.classify import PositiveNaiveBayesClassifier

All_files=[]
for i in range(1,11):
	for j in listdir('data/part'+str(i)):
		All_files.append('data/part'+str(i)+'/'+j)

spam = []
nSpam= []
for i in All_files:
	if i[11:14]=='spm' or i[12:15]=='spm':
		myfile = open(i,'r')
		spam.append(' '.join([line.replace('\n', '') for line in myfile.readlines()]))
	else:
		myfile = open(i,'r')
   		nSpam.append(' '.join([line.replace('\n', '') for line in myfile.readlines()]))

def features(sentence):
	words = sentence.lower().split()
	return dict(('constains(%s)'%w,True) for w in words)

nSpamSet = list(map(features,nSpam))
spamSet  = list(map(features,spam))

classifier =PositiveNaiveBayesClassifier.train(nSpamSet,spamSet)

print classifier.classify(features(nSpam[15]))