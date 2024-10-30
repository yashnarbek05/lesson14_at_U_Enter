import random


def generate_pas(file_location):
    password = ""
    with open(file_location) as file:
        words = file.read()
        word1 = ""
        word2 = ""
        while not (len(word1) > 3 and len(word2) > 3 and (8 <= len(word1 + word2) <= 10)):
            word1 = random.choice(words.split())
            word2 = random.choice(words.split())
    password = word1 + word2
    return password.upper()


if __name__ == '__main__':
    print(generate_pas("input.txt"))
