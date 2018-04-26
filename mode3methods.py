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

def AskingDishQuery(list_ingredient):
    iteration = 0
    i = BooleanAnswer.NO
    liste_information = []
    
    print("[CuistoBot] Please, describe what type of dish do you want. (ingredient, cooking method, adjective, etc.)\n")    
    
    while(i == BooleanAnswer.NO or i == BooleanAnswer.UNKNOW):
        if iteration != 0 and iteration%2 == 0 and i == BooleanAnswer.UNKNOW:
            print("[CuistoBot] Is that all?\n")
        elif iteration%2 == 1 and i == BooleanAnswer.UNKNOW:
            print("[CuistoBot] Ok, Have you finished?\n")
        elif i == BooleanAnswer.NO:
            print("[CuistoBot] Ok, what else?\n")

        parole = input()

        parole_parsee = parseur.parsage(parole)
        
        parole_parsee = tanslate_message(parole_parsee)
        
        for phrase in parole_parsee:
            for mot in phrase:
                if mot in list_ingredient:
                    if mot not in liste_information:
                        liste_information.append(mot)
        
        if iteration != 0:
            i = BooleanAnswer.booleanAnswer(parole_parsee)
                
        iteration += 1
    
    #print(liste_information)
    
    return liste_information

def AskingDishQueryReaction(liste_information):
    print("[CuistoBot] Hm... So I gonna check a delicious dish with these caracteristics:")    
    
    if len(liste_information) == 0:
        print("[CuistoBot] Huh!?.... I'm terribly sorry, but I didn't find any valuable information in your answers.")
        print("[CuistoBot] Maybe, you should repeat... with more... accurate criteria.")
        return True
    else:
        string = "[CuistoBot] "
        for i in range(0, len(liste_information)):
            string += liste_information[i]+" "
        print(string)
        print("[CuistoBot] Let me 2ms, I'm checking my cooking book.")
        return False

def DishResultReaction(resultat, list_ingredient):
    if len(resultat) == 0:
        print("[CuistoBot] Hey, it's interesting! Your choices are really original!...............")
        print("[CuistoBot] Maybe, a little bit too much... I haven't found a dish that correspond to your expections.")
        print("[CuistoBot] Do you want to try again?\n")
        i = BooleanAnswer.booleanAnswer(parseur.parsage(input()))
        while(i == BooleanAnswer.UNKNOW):
            print("[CuistoBot] I didn't understand. Can you repeat, please?\n")
            i = BooleanAnswer.booleanAnswer(parseur.parsage(input()))

        if BooleanAnswer.booleanAnswer(parseur.parsage(input())) == BooleanAnswer.NO:
            return resultat
        else:
            return researchDish(list_ingredient)           

    elif len(resultat) > 0 and len(resultat) < 10:
        print("[CuistoBot] Ok good, I have found "+str(len(resultat))+" dishes. \(^^)/\n")
        return resultat
    else:
        print("[CuistoBot] Ok good, I have found "+str(len(resultat))+" dishes. It's a bigger number! I'll take only 10 dishes, it will be better. \(^^)/\n")
        return resultat

def researchDish(list_ingredient):
    liste_information = AskingDishQuery(list_ingredient)
    
    while(AskingDishQueryReaction(liste_information)):
        liste_information = AskingDishQuery(list_ingredient)
    
    resultat = []
    iteration = 0
    reader = csv.reader(open("epi_r.csv","r"), delimiter=',', quotechar='|')
    categories = parseur.quelle_categorie_observee(liste_information)
    
    for row in reader:
        if iteration == 0:
            iteration += 1

        else:
            couple_plat_point = []
            point = 0
            
            #print(row[0]+" "+str(iteration)+" "+str(len(row[0]))+" "+str(len(row)))
            
            if len(row[0]) != 0:
                for i in categories:
                    point += int(row[i][0])
                
                #if point >= int(len(categories)) and point > 0:
                if point > int(len(categories)/2):
                    couple_plat_point.append(row[0])
                    couple_plat_point.append(point)
                    couple_plat_point.append(iteration+1)
                    resultat.append(couple_plat_point)
            iteration += 1
            
    return DishResultReaction(resultat, list_ingredient)

def tanslate_message(parole):
    
    for phrase in parole:
        for mot in range(0,len(phrase)):
            if(phrase[mot] == "anchovies"):
                phrase[mot] ="anchovy"
            elif(phrase[mot] == "aniseed"):
                phrase[mot] ="anise"
            elif(phrase[mot] == "apples"):
                phrase[mot] ="apple"
            elif(phrase[mot] == "apricots"):
                phrase[mot] ="apricot"
            elif(phrase[mot] == "artichokes"):
                phrase[mot] ="artichoke"
            elif(phrase[mot] == "avocados"):
                phrase[mot] ="avocado"
            elif(phrase[mot] == "bacons"):
                phrase[mot] ="bacon"
            elif(phrase[mot] == "bananas"):
                phrase[mot] ="banana"
            elif(phrase[mot] == "beans"):
                phrase[mot] ="bean"
            elif(phrase[mot] == "beefs"):
                phrase[mot] ="beef"
            elif(phrase[mot] == "beers"):
                phrase[mot] ="beer"
            elif(phrase[mot] == "berries"):
                phrase[mot] ="berry"
            elif(phrase[mot] == "biscuits"):
                phrase[mot] ="biscuit"
            elif(phrase[mot] == "broccolis"):
                phrase[mot] ="broccoli"
            elif(phrase[mot] == "brownies"):
                phrase[mot] ="brownie"
            elif(phrase[mot] == "burritos"):
                phrase[mot] ="burrito"
            elif(phrase[mot] == "caked"):
                phrase[mot] ="cake"
            elif(phrase[mot] == "candies"):
                phrase[mot] ="candy"
            elif(phrase[mot] == "cantaloup"):
                phrase[mot] ="cantaloupe"
            elif(phrase[mot] == "carrots"):
                phrase[mot] ="carrot"
            elif(phrase[mot] == "cheesed"):
                phrase[mot] ="cheese"
            elif(phrase[mot] == "cherries"):
                phrase[mot] ="cherry"
            elif(phrase[mot] == "chickens"):
                phrase[mot] ="chicken"
            elif(phrase[mot] == "chickpeas"):
                phrase[mot] ="chickpea"
            elif(phrase[mot] == "chilies" or phrase[mot] == "chiles"):
                phrase[mot] ="chili"
            elif(phrase[mot] == "chocolates"):
                phrase[mot] ="chocolate"
            elif(phrase[mot] == "cinnamons"):
                phrase[mot] ="cinnamon"
            elif(phrase[mot] == "citruses"):
                phrase[mot] ="citrus"
            elif(phrase[mot] == "clammed"):
                phrase[mot] ="clam"
            elif(phrase[mot] == "clovers" or phrase[mot] == "clover"):
                phrase[mot] ="clove"
            elif(phrase[mot] == "crumble" or phrase[mot] == "cobbler"):
                phrase[mot] ="cobbler/crumble"
            elif(phrase[mot] == "cocktails"):
                phrase[mot] ="cocktail"
            elif(phrase[mot] == "coconuts"):
                phrase[mot] ="coconut"
            elif(phrase[mot] == "coffees"):
                phrase[mot] ="coffee"
            elif(phrase[mot] == "cods"):
                phrase[mot] ="cod"
            elif(phrase[mot] == "cognac" or phrase[mot] == "armagnac"):
                phrase[mot] ="cognac/armagnac"
            elif(phrase[mot] == "corns"):
                phrase[mot] ="corn"
            elif(phrase[mot] == "crab"):
                phrase[mot] ="crab"
            elif(phrase[mot] == "cranberries"):
                phrase[mot] ="cranberry"
            elif(phrase[mot] == "crêpes"):
                phrase[mot] ="crêpe"
            elif(phrase[mot] == "cucumbers"):
                phrase[mot] ="cucumber"
            elif(phrase[mot] == "cupcakes"):
                phrase[mot] ="cupcake"
            elif(phrase[mot] == "ducks"):
                phrase[mot] ="duck"
            elif(phrase[mot] == "eggs"):
                phrase[mot] ="egg"
            elif(phrase[mot] == "fishes"):
                phrase[mot] ="fish"
            elif(phrase[mot] == "frittatas" or phrase[mot] == "frittate"):
                phrase[mot] ="frittata"
            elif(phrase[mot] == "fruits"):
                phrase[mot] ="fruit"
            elif(phrase[mot] == "grill" or phrase[mot] == "barbecue"):
                phrase[mot] ="grill/barbecue"
            elif(phrase[mot] == "geese"):
                phrase[mot] ="goose"
            elif(phrase[mot] == "grapes"):
                phrase[mot] ="grape"
            elif(phrase[mot] == "grapefruits"):
                phrase[mot] ="grapefruit"
            elif(phrase[mot] == "hams"):
                phrase[mot] ="ham"
            elif(phrase[mot] == "hamburgers"):
                phrase[mot] ="hamburger"
            elif(phrase[mot] == "herbs"):
                phrase[mot] ="herb"
            elif(phrase[mot] == "kiwis"):
                phrase[mot] ="kiwi"
            elif(phrase[mot] == "legumes"):
                phrase[mot] ="legume"
            elif(phrase[mot] == "lemons"):
                phrase[mot] ="lemon"
            elif(phrase[mot] == "lingonberries"):
                phrase[mot] ="lingonberry"
            elif(phrase[mot] == "meats"):
                phrase[mot] ="meat"
            elif(phrase[mot] == "melons"):
                phrase[mot] ="melon"
            elif(phrase[mot] == "muffins"):
                phrase[mot] ="muffin"
            elif(phrase[mot] == "mushrooms"):
                phrase[mot] ="mushroom"
            elif(phrase[mot] == "nuts"):
                phrase[mot] ="nut"
            elif(phrase[mot] == "octopuses"):
                phrase[mot] ="octopus"
            elif(phrase[mot] == "olives"):
                phrase[mot] ="olive"
            elif(phrase[mot] == "omelets"):
                phrase[mot] ="omelet"
            elif(phrase[mot] == "onions"):
                phrase[mot] ="onion"
            elif(phrase[mot] == "oranges"):
                phrase[mot] ="orange"
            elif(phrase[mot] == "pastas"):
                phrase[mot] ="pasta"
            elif(phrase[mot] == "peas"):
                phrase[mot] ="pea"
            elif(phrase[mot] == "peaches"):
                phrase[mot] ="peach"
            elif(phrase[mot] == "pears"):
                phrase[mot] ="pear"
            elif(phrase[mot] == "peppers"):
                phrase[mot] ="pepper"
            elif(phrase[mot] == "pies"):
                phrase[mot] ="pie"
            elif(phrase[mot] == "pineapples"):
                phrase[mot] ="pineapple"
            elif(phrase[mot] == "pizzas"):
                phrase[mot] ="pizza"
            elif(phrase[mot] == "potatoes"):
                phrase[mot] ="potato"
            elif(phrase[mot] == "prunes"):
                phrase[mot] ="prune"
            elif(phrase[mot] == "pumpkins"):
                phrase[mot] ="pumpkin"
            elif(phrase[mot] == "rabbits"):
                phrase[mot] ="rabbit"
            elif(phrase[mot] == "raisins"):
                phrase[mot] ="raisin"
            elif(phrase[mot] == "rices"):
                phrase[mot] ="rice"
            elif(phrase[mot] == "salads"):
                phrase[mot] ="salad"
            elif(phrase[mot] == "salmons"):
                phrase[mot] ="salmon"
            elif(phrase[mot] == "sausages"):
                phrase[mot] ="sausage"
            elif(phrase[mot] == "sherries"):
                phrase[mot] ="sherry"
            elif(phrase[mot] == "steaks"):
                phrase[mot] ="steak"
            elif(phrase[mot] == "strawberries"):
                phrase[mot] ="strawberry"
            elif(phrase[mot] == "tomatoes"):
                phrase[mot] ="tomato"
            elif(phrase[mot] == "tunas"):
                phrase[mot] ="tuna"
            elif(phrase[mot] == "vegetables"):
                phrase[mot] ="vegetable"
            elif(phrase[mot] == "watermelons"):
                phrase[mot] ="watermelon"
            elif(phrase[mot] == "turkeys"):
                phrase[mot] ="turkey"

    return parole
        
        