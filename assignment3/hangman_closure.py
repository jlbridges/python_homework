#Declare a function called make_hangman() that has one argument called secret_word. It should also declare an empty array called guesses.
def make_hangman(secret_word):
    guesses = []

    #Within the function declare a function called hangman_closure() that takes one argument, which should be a letter.
    def hangman_closure(letter):
        #Within the inner function, each time it is called, the letter should be appended to the guesses array.
        guesses.append(letter)
        display = "".join(c if c in guesses else "_" for c in secret_word)
        print(display)
        return all(c in guesses for c in secret_word)
    return hangman_closure


secret_word = input("Enter the secret word: ")
guess_letter = make_hangman(secret_word)

solved = False
while not solved:
    letter = input("Guess a letter: ")
    solved = guess_letter(letter)






