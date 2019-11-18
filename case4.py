language = input('Выберете язык: 1.Русский 2. English ')
if language == '2':
    x = str(input()).lower()
    b = list(x)
    sentences = (x.count('.'))
    sum_of_words = (x.count(' ') + 1)
    slogs = len([1 for x in b if x in ['a', 'e', 'i', 'o', 'u', 'y']])
    print('Количество предложений:', sentences)
    print('Слов:', sum_of_words)
    print('Слогов:', slogs)
    average_of_words = sum_of_words / sentences
    print('Средняя длина предложения в словах:', average_of_words)
    average_of_slogs = slogs / sum_of_words
    print('Средняя длина слова в слогах:', average_of_slogs)
elif language == '1':
    y = str(input()).lower()
    b = list(y)
    sentences = (y.count('.'))
    sum_of_words = (y.count(' ') + 1)
    slogs = len([1 for x in b if x in ['а', 'у', 'е', 'о', 'я', 'и', 'ы', 'ю', 'э', 'ё']])
    print('Количество предложений:', sentences)
    print('Слов:', sum_of_words)
    print('Слогов:', slogs)
    average_of_words = sum_of_words / sentences
    print('Средняя длина предложения в словах:', average_of_words)
    average_of_slogs = slogs / sum_of_words
    print('Средняя длина слова в слогах:', average_of_slogs)