#Case-study №4
#Developers: Mauter A. (40%)
#            Kuzmin E. (40%)
#            Petrov V. (20%)

import rulocal as ru
from textblob import TextBlob
language = input(ru.Choose_a_language_Russian_English)
if language == '2':
    text = str(input()).lower()
    b = list(text)
    sentences = text.count('.')                                        #Average of the sentences.
    sum_of_words = (text.count(' ') + 1)                               #Average of the slogs in the slogs.
    slogs = len([1 for x in b if x in ['a', 'e', 'i', 'o', 'u', 'y']])
    print(ru.number_of_offers, sentences)
    print(ru.words, sum_of_words)
    print(ru.syllables, slogs)
    average_of_words = sum_of_words / sentences                        #How much words in the sentences, middiatly.
    print(ru.Average_sentence_length_in_words, average_of_words)
    average_of_slogs = slogs / sum_of_words                            #How much slogs in the words, middiatly.
    print(ru.Average_syllable_length, average_of_slogs)
    TXB = TextBlob(text)
    sentiment = TXB.sentiment.polarity
    subjectivity = TXB.sentiment.subjectivity
    print((1-subjectivity)*100, '%')
    if sentiment < 0:
        print('Негативный текст')
    if 0 < sentiment < 50:
        print('Нейтральный текст')
    if sentiment > 100:
        print('Позитивный текст')
elif language == '1':
    text1 = str(input()).lower()
    b = list(text1)
    sentences = (text1.count('.'))                                      #Average of the sentences.
    sum_of_words: int = (text1.count(' ') + 1)                          #Average of the slogs in the slogs.
    slogs = len([1 for x in b if x in ['а', 'у', 'е', 'о', 'я', 'и', 'ы', 'ю', 'э', 'ё']])
    print(ru.number_of_offers, sentences)
    print(ru.words, sum_of_words)
    print(ru.syllables, slogs)
    average_of_words = sum_of_words / sentences                         #How much words in the sentences, middiatly.
    print(ru.Average_sentence_length_in_words, average_of_words)
    average_of_slogs = slogs / sum_of_words                             #How much slogs in the words, middiatly.
    print(ru.Average_syllable_length, average_of_slogs)
