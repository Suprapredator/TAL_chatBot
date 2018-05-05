# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 09:53:08 2018

@author: supra
"""

from enum import Enum

# Permet de savoir si un message est une question ou non, si oui de quel type.
# Inutilisé actuellement mais utile pour de futurs améliorations.
class QuestionType(Enum):
    WHAT = 0
    HOW = 1
    HOW_MANY = 2
    WHO = 3
    WHERE = 4
    WHY = 5
    WHEN = 6
    NO_QUESTION = -1
    
    def questionType(paroleParsee):
        for phrase in paroleParsee:
            for mot in range(0,len(phrase)):
                if(phrase[mot] == "what"):
                    return QuestionType.WHAT
                elif(phrase[mot] == "who"):
                    return QuestionType.WHO
                elif(phrase[mot] == "why"):
                    return QuestionType.WHY
                elif(phrase[mot] == "where"):
                    return QuestionType.WHERE
                elif(phrase[mot] == "when"):
                    return QuestionType.WHEN
                elif(phrase[mot] == "how" and mot+1 < len(phrase)):
                    if(phrase[mot+1] == "much" or phrase[mot+1] == "many"):
                        return QuestionType.HOW_MANY
                    else:
                        return QuestionType.HOW
        return QuestionType.NO_QUESTION

# Enumération utilisée pour lancer le mode 3.
# Son fonctionnement est identique au mode 2 : si on reconnait un mot dans la liste alors le message appartient au theme.
# Comme nous avons une enumeration, nous pourvons ajouter d'autres themes qui pouront être utile par la suite.
class Sentencetheme(Enum):
    DISH = 1
    UNKNOW = -1
    
    def questionTheme(paroleParsee):
        dish = ["dish","course","speciality","eat","recipe","make","cook","prepare"]
        
        for phrase in paroleParsee:
            for mot in phrase:
                if mot in dish:
                    return Sentencetheme.DISH
        return Sentencetheme.UNKNOW

# Fonction permettant de savoir si un message est affirmatif ou négatif.
class BooleanAnswer(Enum):
    YES = 0
    NO = 1
    UNKNOW = -1
    
    def booleanAnswer(paroleParsee):
        yes = ["yes","ok"]
        no = ["no","nop"]
        
        for phrase in paroleParsee:
            for mot in phrase:
                if mot in yes:
                    return BooleanAnswer.YES
                elif mot in no:
                    return BooleanAnswer.NO
        return BooleanAnswer.UNKNOW