# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 12:10:50 2018

@author: supra
"""

from enumeration import BooleanAnswer
import parseur
import csv

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
    

    resultat = []
    iteration = 0
    reader = csv.reader(open("epi_r.csv","r"), delimiter=',', quotechar='|')
    categories = parseur.quelle_categorie_observee(liste_information)
    
    for row in reader:
        if iteration == 0:
            iteration += 1
            for i in categories:
                print(row[i])
        else:
            couple_plat_point = []
            point = 0
            
            #print(row[0]+" "+str(iteration)+" "+str(len(row)))
            for i in categories:
                point += int(row[i][0])
            
            if point >= int(len(categories)) and point > 0:
                couple_plat_point.append(row[0])
                couple_plat_point.append(point)
                resultat.append(couple_plat_point)
            iteration += 1

        
    print(resultat)
        
        
        
        