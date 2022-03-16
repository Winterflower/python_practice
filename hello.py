print('Hello I am a Python file! It\'s nice to meet you!')
number1 = int(input())
number2 = int(input())


def add(number1, number2):
    return number1 + number2


print(add(number1, number2))


word = input()


def check_letter(word):
    word_counter = 0
    for letter in word:
        if letter == 'a':
            word_counter += 1
    return word_counter

print(f'The letter a appears {check_letter(word)} times in the word {word}')