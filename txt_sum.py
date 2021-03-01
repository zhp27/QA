# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 22:13:29 2021

@author: raha_
"""

import spacy
from spacy.lang.pt.stop_words import STOP_WORDS
from sklearn.feature_extraction.text import CountVectorizer
nlp = spacy.load("en_core_web_sm")
'''with open("data.txt", "r", encoding="utf-8") as f:
        text = " ".join(f.readlines())'''
       
#creat summary of the text
def text_summ(text):
    doc=''.join(str(e) for e in text)
    doc = nlp(doc)
    ''' divide text into sentences 
    convert them to a matrix of token counts.
    create a dictionary that contains the extracted wordsand
    their respective frequencies.
    discarding unnecessary words
   '''
    corpus = [sent.text.lower() for sent in doc.sents ]
    cv = CountVectorizer(stop_words=list(STOP_WORDS))   
    cvFit=cv.fit_transform(corpus)    
    wordList = cv.get_feature_names();    
    countList = cvFit.toarray().sum(axis=0)
    wordFreq=freq_Calc(doc, wordList,countList)
    # Ranking sentences based on frequency
    sentenceRank={}
    for sent in doc.sents:
        for word in sent :       
            if word.text.lower() in wordFreq.keys():            
                if sent in sentenceRank.keys():
                    sentenceRank[sent]+=wordFreq[word.text.lower()]
                else:
                    sentenceRank[sent]=wordFreq[word.text.lower()]
    topSentences=(sorted(sentenceRank.values())[::-1])
    #summarization rate=50%
    sPercent=int(len(topSentences)/2)   
    topSent=topSentences[:sPercent]
    summary=[]
    strsummary=''
    strtemp='' 
    for sent,strength in sentenceRank.items():  
        if strength in topSent:
            summary.append(sent)            
        else:
            continue
        
   
    for row in summary:       
       strtemp=str(row)       
       strsummary+=strtemp
    return strsummary
    
def freq_Calc(doc, wordList,countList):
    wordFreq = dict(zip(wordList,countList))
    val=sorted(wordFreq.values())
    higherWordFrequencies = [word for word,freq in wordFreq.items() if freq in val[-3:]]
    #print("\nWords with higher frequencies: ", higher Word Frequencies)
    # gets relative frequency of words
    higherFR = val[-1]
    for word in wordFreq.keys():  
        wordFreq[word] = (wordFreq[word]/higherFR)

    return wordFreq
