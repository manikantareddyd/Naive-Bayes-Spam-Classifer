import numpy as np
from os import listdir
import nltk
from email import message_from_string
from BeautifulSoup import BeautifulSoup as BS
from re import split
import sys 

###############################################################################
#Misc INIT
dirList=[1,2,3,4,5,6,7,8,9,10]
dirList.remove(int(sys.argv[1]))
stop = nltk.corpus.stopwords.words('english')
lemmatizer=nltk.stem.WordNetLemmatizer()
#############################################################################
All_files=[]
for i in [1,2,3,4,5,6,7,8,9]:
	for j in listdir('data/part'+str(i)):
		All_files.append('data/part'+str(i)+'/'+j)

mails=[]
for i in All_files:
	if i[11:14]=='spm' or i[12:15]=='spm':
		mails.append(
			dict(mail=open(i,'r').read().strip(), category='spam')
			)
	else:	
		mails.append(
			dict(mail=open(i,'r').read().strip(), category='nspam')
			)

for n in range(len(mails)):
  html = mails[n]['mail']
  text = ' '.join(BS(html).findAll(text=True))
  mails[n]['words'] =[lemmatizer.lemmatize(i) for i in split('\W+', text) if i not in stop]

##############################################################################
test_files=[]
for i in [int(sys.argv[1])]:
	for j in listdir('data/part'+str(i)):
		test_files.append('data/part'+str(i)+'/'+j)

test_mails=[]
for i in test_files:
	if i[11:14]=='spm' or i[12:15]=='spm':
		test_mails.append(
			dict(mail=open(i,'r').read().strip(), category='spam')
			)
	else:
		test_mails.append(
			dict(mail=open(i,'r').read().strip(), category='nspam')
			)

for n in range(len(test_mails)):
  html = test_mails[n]['mail']
  text = ' '.join(BS(html).findAll(text=True))
  test_mails[n]['words'] =[lemmatizer.lemmatize(i) for i in split('\W+', text) if i not in stop]

###############################################################################

all_words = nltk.FreqDist(w.lower() for d in mails for w in d['words'])
word_features = all_words.keys()[:2000]

def features(mail):
  mail_words = set(mail['words'])
  features = {}
  for word in word_features:
    features['contains(%s)' % word] = (word in mail_words)
  return features

featuresets = [(features(d), d['category']) for d in mails]
classifier = nltk.NaiveBayesClassifier.train(featuresets)

################################################################################

test_featuresets = [(features(d), d['category']) for d in test_mails]

c=0
c_s=0
c_ns=0
c_ws=0
c_wns=0
for i in range(len(test_mails)):
	t_value=classifier.classify(test_featuresets[i][0])
	if test_featuresets[i][1]=='spam': 
		c_s=c_s+1
	else:
		c_ns=c_ns+1
	po=0
	if test_featuresets[i][1]!=str(t_value):
		c=c+1
		if t_value=='nspam':
			c_ws=c_ws+1
		else:
			c_wns=c_wns+1
#################################################################################

print "#"*24
print "Running on part",sys.argv[1]
print "Total Mails:",len(test_mails)
print "Total Spam:", c_s
print "Total nSpam:", c_ns
print "Total Misclassified:"+str(c)
print "Misclassified Spam:"+str(c_ws)
print "Misclassified nSpam:"+str(c_wns)
