# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 14:37:08 2018

@author: supra
"""

import argparse
import random
import parseur

def discussion_mode_1():
    
    backchannels = ["hm...","I see.","Indeed.","I agree.","ZzZzZzZz.","\"Quand l'appétit va, tout va !\" Obélix 1968"]
    old_backchannels = -1
    new_backchannels = -1
    parole = ""
    
    while(parole != "Au revoir."):
        parole = input()
        
        if(parole != "Au revoir."):
            while(old_backchannels == new_backchannels):
                new_backchannels = int(random.random()*6);
            print("[ChatBot] "+backchannels[new_backchannels])
        else:
            print("[ChatBot] "+"Au revoir.")
        old_backchannels = new_backchannels

def discussion_mode_2():
    
    health = ["sick","ill","cancer","hurt","cold","diarrhea","disease","illness","sickness","malady"]
    family = ["dad","mom","father","mother","sister","brother","uncle","aunt","family","grandfather","grandmother"]
    money = ["dollars","euros","rich","salary","gold","silver","spend","bank","coin","bill"]
    lazy = ["bed","sleep","holydays","lazy","slackness","work","hard","tired","tiresome"]
    heathstone = ["card","play","quest","package","deck","minion","hero","power","hearthstone"]
    
    health_answer = ["You're feeling good?","Have you been sick recently?"]
    family_answer = ["How is your family?","Do "]
    
    answers = {"family":"Family is important, isn't it?","family":"Do you like your family?"}
    print(answers["family"])
    parole = ""
    
    while(parole != "Au revoir."):
        parole = input()
        
        if(parole != "Au revoir."):
            parseur.parsage(parole)
        else:
            print("[ChatBot] "+"Au revoir.")


# _____________________________________________________________________________

if __name__ == "__main__":
    
    print("***CUISTOBOT***\n")    
    
    parser = argparse.ArgumentParser()
    parser.add_argument('mode')
    args = parser.parse_args()
    
    if args.mode == "1":
        print("mode n°1 selectionne")
        discussion_mode_1()
    elif args.mode == "2":
        print("mode n°2 selectionne")
        discussion_mode_2()
    elif args.mode == "3":
        print("mode n°3 selectionne")
    else:
        print("Paramètres invalide !")
    