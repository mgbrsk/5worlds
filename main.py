with open("russian.txt") as file:
    lines = [line.rstrip() for line in file]
words_5 = [w for w in lines if len(w) == 5]
print(f'{len(lines)=}, {len(words_5)=}')
import random
print(random.sample(words_5, 50))


def filter_letters(word_dictionary, letter_list, wrong_letters, true_letters):
    # Убираем если нет нужных букв.
    orig_len = len(word_dictionary)
    if letter_list:
        for letter_param in letter_list:
            print(letter_param)
            word_dictionary = [x for x in word_dictionary if x.find(letter_param[0]) != -1]
            orig_len_2 = len(word_dictionary)
        
        print(f'orig len = {orig_len}, after 1 cleaning = {orig_len_2}')
    # Убираем не на том месте
    full_filter = []
    if letter_list:
        for letter_param in letter_list:
            if letter_param[1] == 1:
                word_dictionary = [x for x in word_dictionary if x[0:1] != letter_param[0]]
            else:
                word_dictionary = [x for x in word_dictionary if x[letter_param[1] - 1:letter_param[1]] != letter_param[0]]
            orig_len_3 = len(word_dictionary)
        print(f'orig len 1 = {orig_len_2}, after 2 cleaning = {orig_len_3}')

    else:
        orig_len_3 = len(word_dictionary)
    
    # Убираем если есть ненужные буквы.
    for letter in wrong_letters:
        print(letter)
        word_dictionary = [x for x in word_dictionary if x.find(letter) == -1]
        orig_len_4 = len(word_dictionary)
    print(f'orig len 2 = {orig_len_3}, after 3 cleaning = {orig_len_4}')
    
    # Оставляем где только нужные буквы
    if true_letters:
        for letter in true_letters:
            print(letter)
            word_dictionary = [x for x in word_dictionary if x[letter[1] - 1] == letter[0]]
    return word_dictionary

# Буквы, которые есть в слове, позиции в которых их быть не может.
letter_dict = (['а', 2], ['е', 4])
# letter_dict = False
# Букв нет в слове.
wrong_letters = ["ж", "и", "з","н","ь","с","р","п"]
# wrong_letters = False
# Буквы есть в слове на указанной позиции.
# true_letters = (['ь', 5], ['ь', 5])
true_letters = False
full_filter = filter_letters(words_5, letter_dict, wrong_letters, true_letters)
print(full_filter)

