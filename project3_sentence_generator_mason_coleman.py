# The random module's choice method randomly chooses an item in a sequence
from random import choice


# Randomly chooses and returns a sentence type from a list of sentence types
def get_sentence_type(sentence_list):
    return choice(sentence_list)


# Randomly chooses and returns an article from a list of articles
def get_article(article_list):
    return choice(article_list)


# Randomly chooses and returns a noun from a list of nouns
def get_noun(noun_list):
    return choice(noun_list)


# Randomly chooses and returns a verb from a list of verbs
def get_verb(verb_list):
    return choice(verb_list)


# Randomly chooses and returns an adjective from a list of adjectives
def get_adjective(adjective_list):
    return choice(adjective_list)


# Randomly chooses and returns an adverb from a list of adverbs
def get_adverb(adverb_list):
    return choice(adverb_list)

# Randomly chooses and returns a coordinating conjunction from a list of coordinating conjunctions
def get_coordinating_conjunction(c_conjunction_list):
    return choice(c_conjunction_list)

# Randomly chooses and returns a subordinating conjunction from a list of subordinating conjunctions
def get_subordinating_conjunction(s_conjunction_list):
    return choice(s_conjunction_list)

# Calls the sentence component functions and inserts them into a formatted string to create a sentence
def create_sentence():
# Creates an empty string called sentence
    sentence = ""
# Calls the get_sentence_type() function and stores the result as a variable called sentence_type    
    sentence_type = get_sentence_type(sentences)
# If sentence_type is simple_one, retrieve an article, noun, and verb and insert them into sentence
    if sentence_type == 'simple_one':
        sentence = "{} {} {}.".format(get_article(articles), get_noun(nouns), get_verb(verbs))
# If sentence_type is simple_two, retrieve an article, adjective, noun, adverb, and verb and insert them into sentence
    elif sentence_type == 'simple_two':
        sentence = "{} {} {} {} {}.".format(get_article(articles), get_adjective(adjectives), get_noun(nouns), get_adverb(adverbs),
                                            get_verb(verbs))
# If sentence_type is compound_one, retrieve two articles, nouns, verbs, and a coordinating conjunction and insert them into sentence 
    elif sentence_type == 'compound_one':
        sentence = "{} {} {}, {} {} {} {}.".format(get_article(articles), get_noun(nouns), get_verb(verbs), 
                                                   get_coordinating_conjunction(coordinating_conjunctions), get_article(articles), 
                                                   get_noun(nouns), get_verb(verbs))
# If sentence_type is compound_two, retrieve two articles, nouns, verbs, a coordinating conjunction, and an adjective and insert them
# into sentence
    elif sentence_type == 'compound_two':
        sentence = "{} {} {} {}, {} {} {} {}.".format(get_article(articles), get_adjective(adjectives), get_noun(nouns),
                                                      get_verb(verbs), get_coordinating_conjunction(coordinating_conjunctions),
                                                      get_article(articles), get_noun(nouns), get_verb(verbs))
# If sentence_type is complex, retreive two articles, nouns, verbs, an adverb, an adjective, and a subordinating conjunction and
# insert them into sentence
    elif sentence_type == 'complex':
        sentence = "{} {} {} {} {}, {} {} {} {}.".format(get_subordinating_conjunction(subordinating_conjunctions), 
                                                         get_article(articles), get_noun(nouns), get_adverb(adverbs), get_verb(verbs),
                                                         get_article(articles), get_adjective(adjectives), get_noun(nouns), 
                                                         get_verb(verbs))
    
# Returns the completed sentence string in a capitalized format (the first letter is capitalized)
    return sentence.capitalize()
    

# Asks the user how many sentences they want created until they desire to quit
def main():
    # Sets more_sentences to True to begin proceeding while loop
    more_sentences = True 
    while more_sentences:
        # Converts the user's input into an integer
        sentence_number = int(input("How many sentences do you want to create? Enter '0' to quit."))  
        # Calls the create_sentence() function however many times the user requested if a non-zero number is entered
        if sentence_number != 0: 
            for num in range(sentence_number): 
                print(create_sentence())
        # Sets more_sentences to False to terminate the loop if 0 is entered        
        else: 
            more_sentences = False 
        
sentences = ['simple_one', 'simple_two', 'compound_one', 'compound_two', 'complex'] # List of sentence types
nouns = ['taranula', 'cricket', 'scorpion', 'hornworm', 'mealworm'] # List of nouns
articles = ['the', 'a'] # List of articles
adverbs = ['constantly', 'rarely', 'diligently', 'usually', 'quickly', 'slowly', 'reluctantly'] # List of adverbs
verbs = ['eats', 'burrows', 'hides', 'builds', 'attacks', 'molts', 'bites', 'stridulates', 'flees', 'wanders'] # List of verbs
adjectives = ['fast', 'shy', 'docile', 'bold', 'feisty', 'curious', 'formidable', 'naive'] # List of adjectives
coordinating_conjunctions = ['for', 'and', 'but', 'or', 'yet', 'so'] # List of coordinating conjunctions
subordinating_conjunctions = ['while', 'although', 'because', 'when'] # List of subordinating conjunctions

# Calls the main loop
main()