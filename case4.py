import rulocal as ru
language = input('Выберете язык: 1.Русский 2. English ')
if language == '2':
    x = str(input()).lower()
    b = list(x)
    sentences = x.count('.')
    sum_of_words = (x.count(' ') + 1)
    slogs = len([1 for x in b if x in ['a', 'e', 'i', 'o', 'u', 'y']])
    print(ru.number_of_offers, sentences)
    print(ru.words, sum_of_words)
    print(ru.syllables, slogs)
    average_of_words = sum_of_words / sentences
    print(ru.Average_sentence_length_in_words, average_of_words)
    average_of_slogs = slogs / sum_of_words
    print(ru.Average_syllable_length, average_of_slogs)
elif language == '1':
    y = str(input()).lower()
    b = list(y)
    sentences = (y.count('.'))
    sum_of_words: int = (y.count(' ') + 1)
    slogs = len([1 for x in b if x in ['а', 'у', 'е', 'о', 'я', 'и', 'ы', 'ю', 'э', 'ё']])
    print(ru.number_of_offers, sentences)
    print(ru.words, sum_of_words)
    print(ru.syllables, slogs)
    average_of_words = sum_of_words / sentences
    print(ru.Average_sentence_length_in_words, average_of_words)
    average_of_slogs = slogs / sum_of_words
    print(ru.Average_syllable_length, average_of_slogs)