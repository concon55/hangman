import random

# A list of words that
potential_words = ["example", "words", "someone", "can", "guess"]

word = random.choice(potential_words)

# Converts the word to lowercase
word = word.lower()
print(word)

current_word = []
# Make it a list of letters for someone to guess
for i in range(len(word)):
	current_word.append("_")

# Some useful variables
guesses = []
maxfails = 7
fails = 0

final = ""

while fails < maxfails:
	#get input
	print(current_word)
	guess = input("Guess a letter: ")

	if(guess in guesses):
		print("You already guessed that")
	# check if the guess is correct: Is it in the word? If so, reveal the letters!
	else:
		guesses += guess
		if(guess in word):
			for i in range(len(word)):
				if(word[i] == guess):
					current_word[i] = guess
			if(final.join(current_word) == word):
				print(current_word)
				print("You win!")
				break

		else:
			print("Nope! Guess again!")
			fails = fails+1
		print("You have " + str(maxfails - fails) + " tries left!")
