
def affiche_liste(liste):
	for i in liste:
		print "|||" + i + "|||";


def read_paragraph_file(filename):
	res = [];
	my_file = open(filename,"r");
	
	ligne = my_file.read();
	list_paragraph = ligne.split("\n");
	
	for i in list_paragraph:
		i = i.replace('\n','');
		if len(i) != 0:
			res.append(i);
	
	my_file.close();		
	return res;	

def write_paragraph_file(list_para, filename):
	my_file = open(filename,"w");
	
	for i in list_para:
		my_file.write(i);
		my_file.write("\n");
		
	my_file.close();

def read_word_list(filename):
	res = [];
	my_file = open(filename,"r");
	
	ligne = my_file.read();
	list_word = ligne.split("\n");
	
	for i in list_word:
		i = i.replace('\n','');
		if len(i) != 0:
			res.append(i);
	
	my_file.close()
	return res;

def write_file_word_list(list_word, filename):
	my_file = open(filename,"w");
	
	for i in list_word:
		my_file.write(i);
		my_file.write(" ");
		
	my_file.close();

def read_tab_separated_file(filename):
	resbis = [];
	res = [];
	my_file = open(filename,"r");
	
	ligne = my_file.read();
	list_ligne = ligne.split("\n");
	
	for i in list_ligne:
		i = i.replace('\n','');
		if len(i) != 0:
			resbis.append(i);
	
	for i in resbis:
		pronom = [];
		list_pronom = i.split("	");
		
		for y in list_pronom:
			y = y.replace(" ","");
			y = y.replace("	","");
			if len(y) != 0:
				pronom.append(y);
			
		res.append(pronom);
	
	my_file.close()
	return res;

def write_file_tabseparated(liste_wordinfo, filename):
	my_file = open(filename,"w");
	
	for i in liste_wordinfo:
		for y in i:
			my_file.write(y);
			my_file.write(" ");
		my_file.write("\n");

	my_file.close();

def segment_into_sents(paragraph):
	list_phrase = [];
	debut = 0;
	
	print paragraph
	i = 1
	
	while i<len(paragraph):
		if paragraph[i] == '.':
			if i-len(paragraph)+1 < -1 and (paragraph[i+1] == '.' and paragraph[i+2] == '.'):
					i = i+2;
			elif ord(paragraph[i-1]) == ord(paragraph[i-1].lower()):
				if(len(paragraph[debut:i]) != 0):
					list_phrase.append(paragraph[debut:i]);
				if i-len(paragraph)+1 != 0:
					debut = i+1;
		i = i+1;
	
	if paragraph[-1] != '.':
		list_phrase.append(paragraph[debut:]);

	for i in range(0, len(list_phrase)):
		list_phrase[i] = list_phrase[i].strip();
	
	print "resultat separation en phrase:";
	print list_phrase;
	
	return list_phrase;

def tokenise(sentence, language):
	debut = 0;
	sentence_tokenised = [];
	
	for i in range (0, len(sentence)):
		if sentence[i] == ' ':
			sentence_tokenised.append(sentence[debut:i]);
			if i-len(sentence)+1 != 0:
					debut = i+1;
		elif sentence[i] == ',':
			sentence_tokenised.append(sentence[debut:i]);
			sentence_tokenised.append(sentence[i]);
			if i-len(sentence)+1 != 0:
					debut = i+1;
		elif sentence[i] == '\'':
			sentence_tokenised.append(sentence[debut:i+1]);
			if i-len(sentence)+1 != 0:
					debut = i+1;
		elif i-len(sentence)+1 != 0:
			if sentence[i+1] == '.' and not(ord(sentence[i]) != ord(sentence[i].lower()) or sentence[i] == '.'):
				sentence_tokenised.append(sentence[debut:i+1]);
				debut = i+1;
	
	sentence_tokenised.append(sentence[debut:]);
	ok = 1;
		
	return sentence_tokenised
			

def lowercase_sentence(sentence):
	
	for i in range(0, len(sentence)):
		sentence[i] = sentence[i].lower();
	
	return sentence;


list_paragraph = read_paragraph_file("alice.en.paras");

write_paragraph_file(list_paragraph, "resultat_para.txt");

list_word = read_word_list("welsh_places.en.list");

write_file_word_list(list_word, "resultat_word.txt")

list_pronom = read_tab_separated_file("personal_pronouns.fr.tsv");

write_file_tabseparated(list_pronom, "resultat_pronom.txt");

test = segment_into_sents("Time ok. gne non, j'aime... seche-cheveux. Et... aussi M.D.Rlol..");

for i in test:
	print "resultat tokenisation:";
	print tokenise(i, "")
