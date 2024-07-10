import json

print('Welcome to personal Vocabulary application')
print('----------------------------------')

dict_word = {'Word': '','Meaning': ''}

while (True):
    print('Choose option do you prefer')
    print('1.Add new word in to dictionary')
    print('2.Practice Vocabulary')
    print('If you prefer to exit press e')
    user_choice = input('You option: ')
    if (user_choice == 'e'):
        break
    elif (int(user_choice) == 1):
        w_input = input('Word: ')
        m_input = input('Meaning: ')
        dict_word['Word'] = w_input
        dict_word['Meaning'] = m_input
        with open('Word_dictionary.txt', 'a') as word_write:
            word_write.write(str(dict_word))
    elif (int(user_choice) == 2):
        with open('Word_dictionary.txt', 'r') as word_read:
            print(word_read.read())
    else:
        print('Wrong input try again')
        continue