# Task 1
def hello():
    return 'Hello!'
print(hello())


# Task 2
def greet(name):
    return f'Hello, {name}!'
print(greet('Jacob'))


# Task 3
def calc(num1, num2, operator='multiply'):
  try:
      match operator.lower():
        case 'multiply':
          return num1 * num2
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'divide':
            test = num1 / num2
            return test
        case 'modulo':
            return num1 % num2
        case 'int_divide':
            return num1 // num2
        case 'pow':
            return num1 ** num2
  except ZeroDivisionError as e:
      return f'You can\'t divide by 0!'
  except TypeError as e:
      return f'You can\'t multiply those values!'

print(calc(9,1, 'divide'))


# Task 4
def data_type_conversion(value, data_type):
    try:
        match data_type.lower():
            case 'int':
                if type(value) == str and '.' in value:
                    return int(float(value))
                else:
                    return int(value)
            case 'float':
                return float(value)
            case 'str':
                return str(value)
    except ValueError:
        return f'You can\'t convert {value} into a {data_type}.'

print(data_type_conversion("banana", 'int'))


# Task 5
def grade(*args):
    try:
        # validate args
        for i in range(len(args)):
            if 0 <= args[i] <=100:
                continue
            else:
                return f'{args[i]} is not a valid grade. Please enter a grade between 0 and 100.'
        # sum valid args
        total = sum(args)
        avg = total / len(args)

        if avg >= 90:
            return f'A'
        elif avg >= 80:
            return f'B'
        elif avg >= 70:
            return f'C'
        elif avg >= 60:
            return f'D'
        else:
            return f'F'
    except TypeError as e:
        return f'Invalid data was provided.'

print(grade(75,85,95))


# Task 6
def repeat(string, count):
    repeat_string = ''
    for i in range(count):
        repeat_string += string

    return repeat_string

print(repeat('string', 4))


# Task 7
def student_scores(score_type, **kwargs):
   print(kwargs)

print(student_scores('best', alice = 90, tim = 80))
# Task 8
def titleize(words):
    # put all little words in a list
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]

    # split the string by space
    split_words = words.split(" ")

    for i, word in enumerate(split_words):
        # capitalize the first element in the list and the last element in the list
        if i == 0 or i == len(split_words) - 1:
            split_words[i] = word.capitalize()
        # if word in list of little words, keep word lowercase
        elif word.lower() in little_words:
            split_words[i] = word.lower()
        else:
        # if word is not at the beginning or end and is not in little words, capitalize word
            split_words[i] = word.capitalize()

    return " ".join(split_words)
print(titleize('war and peace'))
# Task 9
def hangman(secret, guess):
        new_list = []
        new_str = list(secret)
        split_guess = list(guess)
        for i in range(len(new_str)):
            if new_str[i] not in split_guess:
                new_list.append(new_str[i].replace(new_str[i], '_'))
            else:
                new_list.append(new_str[i])
        return "".join(new_list)




print(hangman(secret = "difficulty", guess = "ic"))
# Task 10
def pig_latin(word):
    vowels = ['a','e','i','o','u']
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    word_list = list(word)

    for i in range(len(vowels)):
        if vowels[i] in word_list[0]:
            word_list.append('ay')
            #break
        elif consonants[i] in word_list[0]:
            word_list.append(word_list[i])
            del word_list[0]
            word_list.append('ay')
            #break
        elif 'qu' in word:
            word_list.append('qu')
            word_list.append('ay')

            break
    return "".join(word_list)

print(pig_latin('herryhay'))