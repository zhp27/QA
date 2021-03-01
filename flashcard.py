# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 22:00:57 2021

@author: raha_
"""
import random
#each flash card session contains half of questions in a row
def convertFlash(question, answer, l,qty):
    sampSize=int(qty)
    if sampSize>int(l/2):
        sampSize=int(l/2)    
    flashDict={}
    rand=random.sample(range(0,l-1),sampSize)
    
    for ind in rand:                
        q=question[ind]
        a=answer[ind]
        flashDict[q]=a
    return flashDict
    
