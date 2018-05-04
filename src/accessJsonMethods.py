import json

#Fonctions pour afficher les informations contenues dans le fichier .json
#Ligne désigne la ligne ou se trouve le plat dans le .csv
#data est le lecteur du fichier .json qu'on a deja ouvert.

#Affiche la liste des ingredients
def listeIngredients(ligne, data):
	i = 2 #decalage initial
	for plat in data["meal"]:
		if i==ligne:
			for aliment in plat["ingredients"]:
				print(aliment)
				
		i+=1
		

#Affiche la description du plat
def descriptionPlat(ligne, data):
	i=2
	for plat in data["meal"]:
		if i==ligne:
			if str(plat["desc"])=="None":
				print("Sorry, there is no description")
			else:
				print(plat["desc"])
		i+=1

#Affiche la recette du plat		
def recettePlat(ligne, data):
	i = 2
	for plat in data["meal"]:
		if i==ligne:
			for etape in plat["directions"]:
				print(etape)
				
		i+=1

#Affiche la quantité de gras dans le plat
def fatPlat(ligne, data):
	i=2
	for plat in data["meal"]:
		if i==ligne:
			print(plat["fat"])
		i+=1

#Affiche le nombre de calories dans le plat
def caloriesPlat(ligne, data):
	i=2
	for plat in data["meal"]:
		if i==ligne:
			print(plat["calories"])
		i+=1

#Affiche la quantité de sel dans le plat
def sodiumPlat(ligne, data):
	i=2
	for plat in data["meal"]:
		if i==ligne:
			print(plat["sodium"])
		i+=1
		
