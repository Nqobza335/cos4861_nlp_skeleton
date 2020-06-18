history = "<s> I am human </s> \
            <s> I am not a stone </s> \
            <s> I I live in Labore <s>"


from collections import defaultdict

def build_conditional_probabilities(corpus):
	"""
	The function takes as its input a corpus string (words separated by 
	spaces) and returns a 2D dictionnary of probabilities P(next|current) of
	seeing a word "next" conditionnaly to seeing a word "current". 
	"""

	# First we parse the string to build a double dimension dictionnary that
	# returns the conditional probabilities.

	# We parse the string to build a first dictionnary indicating for each
	# word, what are the words that follow it in the string. Repeated next
	# words are kept so we use a list and not a set. 

	tokenized_string = corpus.split()
	previous_word = ""
	dictionnary = defaultdict(list)

	for current_word in tokenized_string:
		if previous_word != "":
			dictionnary[previous_word].append(current_word)
		previous_word = current_word
		
	# We know parse dictionnary to compute the probability each observed
	# next word for each word in the dictionnary. 

	for key in dictionnary.keys():
		next_words = dictionnary[key]
		unique_words = set(next_words) # removes duplicated
		nb_words = len(next_words)
		probabilities_given_key = {}
		for unique_word in unique_words:
			probabilities_given_key[unique_word] = \
				float(next_words.count(unique_word)) / nb_words
		dictionnary[key] = probabilities_given_key

	return dictionnary

                            #Run this section (build_conditional_probabilities(history)) 
conditional_probabilities = build_conditional_probabilities(history)
