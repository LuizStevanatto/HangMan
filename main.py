import random
from words import word_list


def get_word():
	word = random.choice(word_list)
	return word.upper()


def play(word):
	word_completion = "_" * len(word)
	guessed = False
	guessed_letters = []
	guessed_words = []
	tries = 6
	print("Vamos Jogar Forca!!!")
	print(display_hangman(tries))
	print(word_completion)
	print("\n")

	while not guessed and tries > 0:
		guess = input("Por favor, adivinhe uma letra ou palavra: ").upper()
		if len(guess) == 1 and guess.isalpha():
			if guess in guessed_letters:
				print("Você já tentou a letra ", guess)
			elif guess not in word:
				print(guess, "não está na palavra")
				tries -= 1
				guessed_letters.append(guess)
			else:
				print("Bom trabalho,", guess, "está na palavra")
				guessed_letters.append(guess)
				word_as_list = list(word_completion)
				indices = [
				    i for i, letter in enumerate(word) if letter == guess
				]
				for index in indices:
					word_as_list[index] = guess
				word_completion = "".join(word_as_list)
				if "_" not in word_completion:
					guessed = True
		elif len(guess) == len(word) and guess.isalpha():
			if guess in guessed_words:
				print("Você já tentou essa palavra", guess)
			elif guess != word:
				print(guess, "não está na palavra.")
				tries -= 1
				guessed_words.append(guess)
			else:
				guessed = True
				word_completion = word
		else:
			print("Não é um palpite válido.")
		print(display_hangman(tries))
		print(word_completion)
		print("\n")
	if guessed:
		print("Parabéns, você adivinhou a palavra! Você ganhou!")
	else:
		print("Desculpe, você ficou sem tentativas. A palavra era " + word +
		      ". Talvez na próxima vez!")


def display_hangman(tries):
	stages = [  # final state: head, torso, both arms, and both legs
	    """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
	    # head, torso, both arms, and one leg
	    """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
	    # head, torso, and both arms
	    """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
	    # head, torso, and one arm
	    """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
	    # head and torso
	    """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
	    # head
	    """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
	    # initial empty state
	    """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
	]
	return stages[tries]


def main():
	word = get_word()
	play(word)
	while input("Jogar novamente? (S/N) ").upper() == "S":
		word = get_word()
		play(word)


if __name__ == "__main__":
	main()
