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
	
	if paragraph[-1] != '.' or paragraph[-1] != '!' or paragraph[-1] != '?':
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

		
	return sentence_tokenised
			

def lowercase_sentence(sentence):
	
	for i in range(0, len(sentence)):
		sentence[i] = sentence[i].lower();
	
	return sentence;

def parsage(parole):
    if parole != "":
        test = segment_into_sents(parole);
        res = []    
        
        for i in test:
        	res.append(tokenise(i, ""))
        
        print(res)
    else:
        res = [[""]]
    
    return res;
