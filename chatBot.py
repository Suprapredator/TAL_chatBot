# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 14:37:08 2018

@author: supra
"""

import argparse
import random

def discussion_mode_1():
    
    backchannels = ["hm...","Je vois.","Effectivement.","Je suis d'accord.","ZzZzZzZz.","...ok."]
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

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('mode')
    args = parser.parse_args()
    
    if args.mode == "1":
        print("mode n°1 selectionne")
        discussion_mode_1()
    elif args.mode == "2":
        print("mode n°2 selectionne")
    else:
        print("mode n°3 selectionne")
    