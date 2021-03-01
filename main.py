# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:03:05 2021

@author: raha_
"""
import flashcard as fc
import qg_NER as qg
from nltk import sent_tokenize

def generateFlashcards(inputText, qty):    
    sent= sent_tokenize(inputText)
    [flashRep,ansRep, l]= qg.flash_Rep(sent)
    FDict=fc.convertFlash(flashRep,ansRep,l,qty)
    return FDict
