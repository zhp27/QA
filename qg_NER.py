# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 22:00:57 2021

@author: raha_
"""

import spacy
from nltk import sent_tokenize
import txt_sum as ts

nlp = spacy.load('en_core_web_sm') 

#Reading the file and breaking it to sentences

#NER
def NER_d(sentence):    
    doc = nlp(sentence) 
    ne=[]
    for ent in doc.ents: 
        ne.append(ent)
       # print(ent.text, ent.start_char, ent.end_char, ent.label_)
        
    return ne
     
def sent_Ref(sent):     
    sent1=[]
    #spilit the text and keep meaningful setntences which have min of one subject
    for s in sent:
        if len(s)>100:
            p=s.split(",",1)
            l=len(p)
            
            for i in range(l):
                subToks=[]
                doc=nlp(p[i])
                subToks = [tok for tok in doc if (tok.dep_ == "nsubj") ]
                if subToks!=[]:
                    sent1.append(p[i])
        elif len(s)>200:
             p=s.split(",",2)
             l=len(p)
             for i in range(l):
                subToks=[]
                doc=nlp(p[i])
                subToks = [tok for tok in doc if (tok.dep_ == "nsubj") ]
                if subToks!=[]:
                    sent1.append(p[i])
               
        else:
             sent1.append(s)
    return sent1
             
def flash_Rep(sent): 
    sents=sent_Ref(sent)
    #create flash repository
    flashRep=[] #Questions repository
    ansRep=[] #Answers repository
    flashCand=''
    for s in sents:
        #NER_d(s)
        doc=nlp(s)
        if len(doc)>4:
            stDoc=str(doc)
            #finding NEs and create questions and answers based on them
            Ne=NER_d(stDoc)
            for nc in Ne:
                #print(nc.text)
                stnc=str(nc.text)
                flashCand=stDoc.replace(stnc," ....... ")
                flashRep.append(flashCand)
                ansRep.append(stnc)
            
    l=len(flashRep)
    #callinf flash card to create random questions from the repository
    return (flashRep,ansRep,l)
    

        
        
        

