# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 14:37:08 2018

@author: supra
"""

import argparse
import random
import parseur
import recipe


def discussion_mode_1(parole, old_backchannels):
    
    backchannels = ["hm...","I see.","Indeed.","I agree.","ZzZzZzZz.","\"Quand l'appétit va, tout va !\" Obélix 1968"]
    new_backchannels = old_backchannels
        
    if(parole != "Bye."):
        while(old_backchannels == new_backchannels):
            new_backchannels = int(random.random()*6);
        
        print("[ChatBot] "+backchannels[new_backchannels])
        return new_backchannels

def discussion_mode_2(parole, old_backchannels):
    
    health = ["sick","ill","cancer","hurt","cold","diarrhea","disease","illness","sickness","malady"]
    family = ["dad","mom","father","mother","sister","brother","uncle","aunt","family","grandfather","grandmother"]
    money = ["dollars","euros","rich","salary","gold","silver","spend","bank","coin","bill"]
    lazy = ["bed","sleep","holydays","lazy","slackness","work","hard","tired","tiresome"]
    hearthstone = ["card","play","quest","package","deck","minion","hero","power","hearthstone"]
    hello = ["hello","hi","hey","yo","dear","afternoon","morning","greetings","up","howdy"]
    
    health_answer = ["You're feeling good?","Have you been sick recently?"]
    family_answer = ["How is your family?","Do you think that \"family\" is important?"]
    money_answer = ["Money is your best friend in this world, isn't it?","What do you think about the congolexicalization of the laws of the market?"]
    lazy_answer = ["Are you tired?","Where do you go last holydays?"]
    hearthstone_answer = ["Do you know the lich king?","What's your level?"]
    hello_answer = ["Greetings!","HHOOWWDDYY!"]
        
    compteur = [0,0,0,0,0,0]
    new_backchannels = old_backchannels
    parole_parser = parseur.parsage(parole)
    
            
    for phrase in parole_parser:
        for mot in health:
            compteur[0] += phrase.count(mot)
                    
        for mot in family:
            compteur[1] += phrase.count(mot)
                    
        for mot in money:
            compteur[2] += phrase.count(mot)
                    
        for mot in lazy:
            compteur[3] += phrase.count(mot)
                    
        for mot in hearthstone:
            compteur[4] += phrase.count(mot)
            
        for mot in hello:
            compteur[5] += phrase.count(mot)
            
        print(compteur)           
            
        max = 0; res = -1;
        for i in range(0,len(compteur)):
            if compteur[i]>max:
                res = i
                max = compteur[i]
        
        while(old_backchannels == new_backchannels):
            new_backchannels = int(random.random()*2);     
        
        if res==0:
            print("[ChatBot] "+health_answer[new_backchannels])
        elif res==1:
            print("[ChatBot] "+family_answer[new_backchannels])
        elif res==2:
            print("[ChatBot] "+money_answer[new_backchannels])
        elif res==3:
            print("[ChatBot] "+lazy_answer[new_backchannels])
        elif res==4:
            print("[ChatBot] "+hearthstone_answer[new_backchannels])
        elif res==5:
            print("[ChatBot] "+hello_answer[new_backchannels])
        else:
            new_backchannels = discussion_mode_1(parole, old_backchannels);
            
        return new_backchannels

def discussion_mode_3(parole, old_backchannels):
    


# _____________________________________________________________________________

if __name__ == "__main__":
    
    print("***CUISTOBOT***\n")
    
    parser = argparse.ArgumentParser()
    parser.add_argument('mode')
    args = parser.parse_args()
    
    parole = ""
    old_backchannels = -1
    
    while(parole != "Bye."):
        parole = input()
        
        if(parole != "Au revoir."):
            if args.mode == "1":
                old_backchannels = discussion_mode_1(parole, old_backchannels)
            elif args.mode == "2":
                old_backchannels = discussion_mode_2(parole, old_backchannels)
            elif args.mode == "3":
                print("lol")
            else:
                print("Paramètres invalide !")
                parole = "Au revoir."
        
        if(parole == "Bye."):
            print("[ChatBot] "+"Bye.")   