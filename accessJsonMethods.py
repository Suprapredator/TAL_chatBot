import json

def listeIngredients(ligne, data):
	i = 2
	for plat in data["meal"]:
		if i==ligne:
			for aliment in plat["ingredients"]:
				print(aliment)
				
		i+=1
		
	
def descriptionPlat(ligne, data):
	i=2
	for plat in data["meal"]:
		if i==ligne:
			if str(plat["desc"])=="None":
				print("Sorry, there is no description")
			else:
				print(plat["desc"])
		i+=1
		
def recettePlat(ligne, data):
	i = 2
	for plat in data["meal"]:
		if i==ligne:
			for etape in plat["directions"]:
				print(etape)
				
		i+=1

def fatPlat(ligne, data):
	i=2
	for plat in data["meal"]:
		if i==ligne:
			print(plat["fat"])
		i+=1

def caloriesPlat(ligne, data):
	i=2
	for plat in data["meal"]:
		if i==ligne:
			print(plat["calories"])
		i+=1

def sodiumPlat(ligne, data):
	i=2
	for plat in data["meal"]:
		if i==ligne:
			print(plat["sodium"])
		i+=1
		
data = json.load(open('full_format_recipes.json'))
#ingredients = listeIngredients(11,data)
descriptionPlat(20126,data)
