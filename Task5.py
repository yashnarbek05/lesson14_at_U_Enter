def misspelled_words(file_location, words):
    mis_words = []

    with (open(file_location) as file):
        text = file.read()
        for word in text.split():

            if word.lower().replace('?', '').replace('.', '') not in words:
                mis_words.append(word)

    return mis_words


if __name__ == '__main__':
    print(misspelled_words("input.txt", ["hello", "you", 'world']))
