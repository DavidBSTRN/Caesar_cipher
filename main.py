def encrypt(message, key):
    new_message = ''

    for letter in message:
        index = alphabet.index(letter)
        new_index = index + key

        new_message = new_message + alphabet[new_index]

    return new_message

def decode(message, key):
    new_message = ''

    for letter in message:
        index = alphabet.index(letter)
        new_index = index - key
        new_message = new_message + alphabet[new_index]

    return new_message

def check_message(message):
    for i in message:
        if i in alphabet:
            pass
        else:
            raise ValueError(f"{i} is not in alphabet")

def frequency_analysis(message):
    text_letter_frequencies = {' ': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0,
                               'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0,
                               'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for char in message:
        text_letter_frequencies[char] += 1

    for char, value in text_letter_frequencies.items():
        text_letter_frequencies[char] = round((value / len(message)) * 100, 2)

    return text_letter_frequencies

def similarity_score(message):
    text_letter_frequency = frequency_analysis(message)

    sim_score = 0

    for char in text_letter_frequency:
        multiply = text_letter_frequency[char] * lang_letter_frequency[char]
        sim_score += multiply

    return sim_score

def sim_score_decode(message):
    key = 0
    shift = 0
    highest_similarity = 0

    for i in range(27, 0, -1):
        sim_score = similarity_score(encrypt(message, shift))
        shift += 1

        if sim_score > highest_similarity:
            highest_similarity = sim_score
            key = i

    return key


if __name__ == "__main__":
    alphabet = [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                "T", "U", "V", "W", "X", "Y", "Z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    english_letter_frequencies = {' ': 20, 'A': 8.17, 'B': 1.49, 'C': 2.78, 'D': 4.25, 'E': 12.70, 'F': 2.23,
                                  'G': 2.02, 'H': 6.09, 'I': 6.97, 'J': 0.15, 'K': 0.77, 'L': 4.03, 'M': 2.41,
                                  'N': 6.75, 'O': 7.51, 'P': 1.93, 'Q': 0.10, 'R': 5.99, 'S': 6.33, 'T': 9.06,
                                  'U': 2.76, 'V': 0.98, 'W': 2.36, 'X': 0.15, 'Y': 1.97, 'Z': 0.07}

    czech_letter_frequencies = {' ': 20, 'A': 8.35, 'B': 1.23, 'C': 4.41, 'D': 3.99, 'E': 9.21, 'F': 0.82,
                                  'G': 1.52, 'H': 1.46, 'I': 6.94, 'J': 2.17, 'K': 3.73, 'L': 3.54, 'M': 3.15,
                                  'N': 6.83, 'O': 6.26, 'P': 2.42, 'Q': 0.01, 'R': 5.87, 'S': 6.02, 'T': 5.05,
                                  'U': 3.41, 'V': 5.23, 'W': 0.02, 'X': 0.03, 'Y': 4.74, 'Z': 4.64}

    lets_continue = True
    while lets_continue:
        state = input("Type 'en' to encode the message, 'de' to decode the message or 'end' for end program:\n")

        if state == "en":
            msg_to_encode = input("Enter the message:\n").upper()
            check_message(msg_to_encode)
            try:
                key = int(input("Enter the key:\n"))
                print(f"Your encrypt message is: {encrypt(msg_to_encode, key)}")
                state = input("Type 'en' to encode the message, 'de' to decode the message or 'end' for end program:\n")
            except ValueError:
                print("Key must be integer!")

        if state == "de":

            language = input("type 'CZ' or 'EN' for choosing language\n")
            if language == "EN":
                lang_letter_frequency = english_letter_frequencies
            elif language == "CZ":
                lang_letter_frequency = czech_letter_frequencies

            msg_to_decode = input("Enter the message:\n").upper()
            check_message(msg_to_decode)

            decode_key = sim_score_decode(msg_to_decode)
            print(f"Encode message is: {decode(msg_to_decode, decode_key)}")

            state = input("Type 'en' to encode the message, 'de' to decode the message or 'end' for end program:\n")

        if state == "end":
            lets_continue = False