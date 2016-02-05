Naïve Bayes Spam Classifier
===========================
Naïve Bayes filter is a simple yet efficient algorithm to classify mails as spam and Non-spam.
It is a generative algorithm in which we make naïve assumption that attributes of an object are mutually independent and can be estimated freely.

In the case of spam classifiers, the attributes of a particular mail are its words. Although we know that a mail is a statement of a language set, implying that the words depend on each other and their order is also a relevant factor to be considered, we ignore it and assume every word in the mail occurs in the mail owing to its distribution function independent of other words in the mail.

We fit a probability distribution for every word based on the frequency distribution of words in the entire learning set Χ (a set of labelled mails). Studies as well as my results show that a Multinomial distribution works well with an accuracy of ~99% compared to a Gaussian fit.
Before the Mails are processed for generating the frequency distribution, we need to clean the mails of erroneous wide spaces, punctuations and html tags and preserve only the words.  

Further experimentations involve pruning the data off the stops words and also lemmatizing it.
By pruning the data with stop words, which happen to be most common words in the language set, we are trying to minimize the effect of common words, whose distribution would usually have higher values, and give a chance to less frequent words which might actually be characteristics of the specific classes.

Though stop words usually refer to the most common words in a language, there is no single universal list of stop words used by all natural language processing tools, and indeed not all tools even use such a list.

In Lemmatizing, as the name suggests, we lemmatize the words to their root, i, e. break and breaking would be lemmatized to break. In this way we are able to identify words that mean the same into ne frequency class. This helps to introduce a semantic element to the classification problem, which initially neglected any order in data.  
The data has been cross validated 10 fold.

 + Precision:   Of all things labelled as spam, how many are actually spam

 + Recall:    Of all things that are truly spam, how many did we label

 + Accuracy:  Of all things, how many did we correctly label


        Results

        Lemmatized words and Trimmed stop words
        |       |           Gaussian              |           Multinomial         |
        |-------|---------------------------------|-------------------------------|
        | Cross | Accuracy | Precision   | Recall | Accuracy | Precision | Recall |
        |-------|----------|-------------|--------|----------|-----------|--------|
        | 1     | 0.93     | 1.00        | 0.58   | 0.99     | 0.96      | 1.00   |
        | 2     | 0.95     | 0.97        | 0.71   | 0.99     | 0.96      | 1.00   |
        | 3     | 0.94     | 1.00        | 0.67   | 0.99     | 0.96      | 1.00   |
        | 4     | 0.93     | 1.00        | 0.60   | 1.00     | 0.98      | 1.00   |
        | 5     | 0.96     | 1.00        | 0.73   | 1.00     | 1.00      | 0.98   |
        | 6     | 0.95     | 1.00        | 0.69   | 1.00     | 1.00      | 1.00   |
        | 7     | 0.95     | 1.00        | 0.71   | 0.99     | 0.98      | 0.98   |
        | 8     | 0.93     | 0.85        | 0.73   | 0.99     | 0.96      | 1.00   |
        | 9     | 0.96     | 1.00        | 0.73   | 0.98     | 1.00      | 0.88   |
        | 10    | 0.95     | 0.97        | 0.71   | 0.99     | 1.00      | 0.94   |


        Trimmed Stopwords
        |       |           Gaussian              |           Multinomial         |
        |-------|---------------------------------|-------------------------------|
        | Cross | Accuracy | Precision   | Recall | Accuracy | Precision | Recall |
        |-------|----------|-------------|--------|----------|-----------|--------|
        | 1     | 0.92     | 0.96        | 0.56   | 0.99     | 0.98      | 0.98   |
        | 2     | 0.94     | 0.97        | 0.65   | 0.99     | 0.96      | 1.00   |
        | 3     | 0.94     | 0.97        | 0.69   | 0.99     | 0.96      | 1.00   |
        | 4     | 0.95     | 1.00        | 0.71   | 1.00     | 0.98      | 1.00   |
        | 5     | 0.95     | 1.00        | 0.71   | 1.00     | 1.00      | 1.00   |
        | 6     | 0.96     | 1.00        | 0.73   | 1.00     | 1.00      | 1.00   |
        | 7     | 0.95     | 1.00        | 0.71   | 1.00     | 1.00      | 0.98   |
        | 8     | 0.94     | 0.92        | 0.71   | 0.99     | 0.94      | 1.00   |
        | 9     | 0.94     | 0.97        | 0.67   | 0.98     | 0.98      | 0.88   |
        | 10    | 0.95     | 0.97        | 0.81   | 0.99     | 1.00      | 0.94   |

        Subject + Body only
        |       |           Gaussian              |           Multinomial         |
        |-------|---------------------------------|-------------------------------|
        | Cross | Accuracy | Precision   | Recall | Accuracy | Precision | Recall |
        |-------|----------|-------------|--------|----------|-----------|--------|
        | 1     | 0.92     | 0.96        | 0.56   | 0.99     | 0.94      | 0.98   |
        | 2     | 0.94     | 0.97        | 0.65   | 0.99     | 0.92      | 1.00   |
        | 3     | 0.94     | 0.97        | 0.69   | 0.99     | 0.96      | 1.00   |
        | 4     | 0.95     | 1.00        | 0.71   | 0.99     | 0.96      | 1.00   |
        | 5     | 0.95     | 1.00        | 0.71   | 1.00     | 1.00      | 1.00   |
        | 6     | 0.96     | 1.00        | 0.73   | 1.00     | 1.00      | 1.00   |
        | 7     | 0.95     | 1.00        | 0.71   | 0.99     | 0.98      | 0.98   |
        | 8     | 0.94     | 0.92        | 0.71   | 0.98     | 0.91      | 1.00   |
        | 9     | 0.94     | 0.97        | 0.67   | 0.99     | 0.98      | 0.98   |
        | 10    | 0.95     | 0.97        | 0.69   | 0.99     | 1.00      | 0.94   |


As can be clearly seen Multinomial Naïve Bayes out performs Gaussian Naïve Bayes.
It can be observed that the precision of classifier, by using a Gaussian Distribution, is high in comparison to the recall in same case. In fact, the recall in Gaussian NB seems pretty low.

Although the accuracy of GaussianNB is over 90%, the MultinomialNB offers nearly perfect predictions. Further reading on this debate suggests that practically MultinomialNB bids over GaussianNB for the particular problem of Text Classification.


NOTE:

 + Naïve Bayes assumes that L is separable, it is invalid otherwise.
 + Detailed Results are present in the other file Raw Results, which includes the confusion matrix and f scores in each specific case.
