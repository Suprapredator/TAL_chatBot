import csv

def segment_into_sents(paragraph):
	list_phrase = [];
	debut = 0;
	
	i = 1
	
	while i<len(paragraph):
		if paragraph[i] == '.' or paragraph[i] == '?' or paragraph[i] == '!':
			if i-len(paragraph)+1 < -1 and (paragraph[i+1] == '.' and paragraph[i+2] == '.'):
					i = i+2;
			elif ord(paragraph[i-1]) == ord(paragraph[i-1].lower()):
				if(len(paragraph[debut:i]) != 0):
					list_phrase.append(paragraph[debut:i]);
				if i-len(paragraph)+1 != 0:
					debut = i+1;
		i = i+1;
	
	if paragraph[len(paragraph)-1] != '.' and paragraph[len(paragraph)-1] != '!' and paragraph[len(paragraph)-1] != '?':
		list_phrase.append(paragraph[debut:]);

	for i in range(0, len(list_phrase)):
		list_phrase[i] = list_phrase[i].strip();
	
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
			sentence_tokenised.append(sentence[debut:i]);
			if i-len(sentence)+1 != 0:
					debut = i;
		elif i-len(sentence)+1 != 0:
			if sentence[i+1] == '.' and not(ord(sentence[i]) != ord(sentence[i].lower()) or sentence[i] == '.'):
				sentence_tokenised.append(sentence[debut:i+1]);
				debut = i+1;
	
	sentence_tokenised.append(sentence[debut:]);

		
	return lowercase_sentence(sentence_tokenised)
			

def lowercase_sentence(sentence):
	
	for i in range(0, len(sentence)):
		sentence[i] = sentence[i].lower();
	
	return sentence;

def nettoyage(sentences):
    for sentence in sentences:
        while(sentence.count("") > 0):
            sentence.remove("")

def parsage(parole):
    if parole != "":
        test = segment_into_sents(parole);
        res = []    
        
        for i in test:
        	res.append(tokenise(i, ""))
         
        nettoyage(res)
        
        #print(res)
    else:
        res = [[""]]
    
    return res;
    
def parsage_data(filename):
    my_file = open(filename,"r");
    ligne = my_file.read();

    liste = ligne.replace('\t','\n');
    liste = ligne.split('\n');
    
    my_file.close();
    return liste;

def quelle_categorie_observee(information):
    tab = []
    data = open("epi_r.csv","r")
    
    reader = csv.reader(data, delimiter=',', quotechar='|')
    
    for row in reader:
        for i in range(6,len(row)):
            if row[i] in information:
                tab.append(i)
        
        return tab