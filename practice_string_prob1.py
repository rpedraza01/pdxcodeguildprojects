#practice_string_prob1.py
def double_letters(word):
    doubled_word_string = ""
    for char in word:
        doubled_word_string += char * 2
    return doubled_word_string
