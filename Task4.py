
def longest_word(file_location):
    longest_words = []
    max_len = 0
    with open(file_location) as file:
        lines = file.readlines()
        for words in lines:
            for word in words.split():
                current_len = len(word)
                if max_len < current_len:
                    max_len = current_len
                    longest_words = [word]
                elif max_len == current_len:
                    longest_words.append(word)
    return longest_words, max_len



if __name__ == '__main__':
    print(longest_word("input.txt"))