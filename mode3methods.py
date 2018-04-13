# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 12:10:50 2018

@author: supra
"""

from enumeration import QuestionType,Sentencetheme,BooleanAnswer
import parseur

def researchRecipe():
    i=0

def researchDish(list_ingredient):
    iteration = 0
    i = BooleanAnswer.NO
    liste_information = []
    
    while(i == BooleanAnswer.NO):
        if iteration == 0:
            print("[ChatBot] Please, describe what type of dish do you want. (ingredient, cooking method, adjective, etc.)\n")
        else:
            print("[ChatBot] Ok, what's else?\n")
        
        parole = input()
        
        parole_parsee = parseur.parsage(parole)
        
        for phrase in parole_parsee:
            for mot in phrase:
                if mot in list_ingredient:
                    if mot not in liste_information:
                        liste_information.append(mot)
        
        print("[ChatBot] Is that all?\n")
        
        i = BooleanAnswer.booleanAnswer(parseur.parsage(input()))
        while(i == BooleanAnswer.UNKNOW):
            print("[ChatBot] I don't understand, is that all?\n")
            i = BooleanAnswer.booleanAnswer(parseur.parsage(input()))
        iteration = 1
        
    print(liste_information)
        
        
        
        