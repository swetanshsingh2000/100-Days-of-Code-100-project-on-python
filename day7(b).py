import random
from hangman_words import word_list
from hangman_art import stages, logo

# Set 'lives' to equal 6.
lives = 6

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#improvong user experience
print(logo)
print(f'Pssst, the solution is {chosen_word}.')

retry= 3
# Creating blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"you have already guessed {guess} this letter!!")
        retry -= 1
        if retry == 0:
            lives=0
            print("u have used all ur retry be better next time")
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
#If the user has entered a letter they've already guessed, print the letter and let them know.


# If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
#  e.g. You guessed d, that's not in the word. You lose a life.

    # TODO-2: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("********************* You WIN *********************")
    if lives == 0:
        end_of_game = True
        print("********************* You lose *********************")
    # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])