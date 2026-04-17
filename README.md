# Project Objectives

* Work with `random` module to create diverse sentences
* Implement functions to handle specific logic
* Use Python lists to represent
  * Grammatical elements (nouns, verbs, adjectives, etc.)
  * Sentence structures (simple, compound, complex)
  * Words for each grammatical element
 
# Design Choices

* **Strings**: I used strings to store the completed sentences because I would be able to use the 
string’s format() method to develop templates for simple, compound, and complex 
sentences and the capitalize() method to properly format the created sentence
* **Lists**: I used lists to store the vocabulary words for each sentence component because lists 
are easy to change
* `while` **Loop**: I used a while loop in the main() function for more user control 

# Implementation Details

1. Defined a function that accepts a list of the different sentence types and randomly 
chooses one with the choice() method 
    * get_sentence_type()
2. Defined a function for each grammatical category that accepts a list of vocab words and 
randomly chooses one with the choice() method 
    * get_article() 
    * get_noun()  
    * get_verb()  
    * get_adjective() 
    * get_adverb() 
    * get_coordinating_conjunction() 
    * get_subordinating_conjunction() 
3. Defined a function that utilizes selection (if and elif statements) to determine what type of 
sentence to create that then calls for the necessary sentence components based on the
template with the format() method 
    * create_sentence() 
4. Defined a function that uses a while loop to handle user input (asks how many sentences 
should be created) and function iteration 
    * main()

# Challenges

* Determining the proper format for each sentence type
* Adding variety and diversity to the sentences

# Insights

* A deeper understanding of the logical structure of the English language
* More experience with manipulating strings and changing program behavior with 
selection
* Breaking a program down into functions
* Application of a new Python module: the random module
