#Declare a function called make_hangman() that has one argument called secret_word. It should also declare an empty array called guesses.
def make_hangman(secret_word):
    guesses = []
    new_str = list(secret_word)
    print(new_str)
    for i in range(len(secret_word)):
        print('_' , end = '')
    #Within the function declare a function called hangman_closure() that takes one argument, which should be a letter.
    def hangman_closure(letter):
        #Within the inner function, each time it is called, the letter should be appended to the guesses array.
        guesses.append(letter)
    return hangman_closure

make_hangman('secret')


# def hangman(secret, guess):
#     new_list = []
#     new_str = list(secret)
#     split_guess = list(guess)
#     for i in range(len(new_str)):
#         if new_str[i] not in split_guess:
#             new_list.append(new_str[i].replace(new_str[i], '_'))
#         else:
#             new_list.append(new_str[i])
#     return "".join(new_list)
#
#
# print(hangman(secret="difficulty", guess="ic"))



