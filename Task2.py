
def letter_frequencies(file_location):
    let_freq = {}

    with open(file_location) as file:
        text = file.read()
        for char in text:
            if 'a' <= char.lower() <= 'z':
                if char.lower() not in let_freq:
                    let_freq[char.lower()] = 1
                else:
                    let_freq[char.lower()] += 1
    return sorted(let_freq.items(), key=lambda x : x[1], reverse=True)





if __name__ == '__main__':
    print(letter_frequencies("input.txt"))