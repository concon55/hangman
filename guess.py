import random

# list of words
potential_words = ["example", "words", "someone", "can", "guess"]
#get a random word from the list
word = random.choice(potential_words)

# Converts the word to lowercase
word = word.lower()

#for testing:
#print(word)

#create an empty list 
current_word = []
#populate the list with number of blanks according to size of the random word
for i in range(len(word)):
	current_word.append("_")

#keep track of guesses
guesses = []
#number of tries
maxfails = 7
fails = 0

#for string conversion
final = ""

while fails < maxfails:
	#get user input
	print(current_word)
	guess = input("Guess a letter: ")

	#check if the user guessed the letter already (check their guesses list)
	if(guess in guesses):
		print("You already guessed that")
	else:
		guesses += guess #if the letter has not been guessed, add it to the guesses list 
		#check if the letter that the user guesses is in the word
		if(guess in word):
			for i in range(len(word)): #compare the guess to each letter in the word 
				if(word[i] == guess): 
					current_word[i] = guess #change the blank to the letter
			 #if the user guesses the entire word, they win 
			if(final.join(current_word) == word): #convert the list of letters into a string for comparison
				print(current_word)
				print("You win!")
				break
		#if the user guesses a wrong letter
		else:
			print("Nope! Guess again!")
			fails = fails+1 #update counter for while loop
		print("You have " + str(maxfails - fails) + " tries left!")
