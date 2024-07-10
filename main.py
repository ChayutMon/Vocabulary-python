import json
import os
import random

def word_game_round(vocabulary):
    if not vocabulary:
        print("No words in the dictionary. Add some words first!\n")
        return
    print("-----------------------------------")
    print('How many rounds do you prefer to play? (At least should be 10 rounds)')
    while True:
        try:   
            g_round = input('Enter number of rounds: ').strip()
            g_round_int = int(g_round)
            if g_round_int < 10:
                print('The number of rounds should be at least 10.')
                continue
            break
        except ValueError:
            print('Invalid input. The input should be a number.')
            
    point = 0
    
    for i in range(g_round_int):
        word, definition = random.choice(list(vocabulary.items()))
        print("-----------------------------------")
        print(f'Round {i+1}')
        print(f"What's the definition of {word}?")
        user_ans = input('The definition is: ').strip()
        
        if user_ans.lower() == definition.lower():
            print('Good job!!\n')
            print("-----------------------------------")
            point += 1
        else:
            print(f"Incorrect! The correct definition is {definition}.\n")
            print("-----------------------------------")
    print("-----------------------------------")
    print(f"Finished the game! You got {point}/{g_round_int}")

def add_word(vocabulary):
    print("-----------------------------------")
    word = input("Enter the new word: ").strip()
    definition = input("Enter the definition: ").strip()
    vocabulary[word] = definition
    print(f"Word '{word}' added successfully!\n")
    print("-----------------------------------")

def practice_vocabulary(vocabulary):
    if not vocabulary:
        print("-----------------------------------")
        print("No words in the dictionary. Add some words first!\n")
        print("-----------------------------------")
        return

    word, definition = random.choice(list(vocabulary.items()))
    print("-----------------------------------")
    print(f"What does this word mean: {word}")
    print("-----------------------------------")
    user_answer = input("What's the definition? ").strip()

    if user_answer.lower() == definition.lower():
        print("-----------------------------------")
        print("Correct!\n")
        print("-----------------------------------")
    else:
        print("-----------------------------------")
        print(f"Incorrect! The word '{word}' means '{definition}'.\n")
        print("-----------------------------------")

def save_vocabulary(vocabulary, filename):
    with open(filename, 'w',encoding='utf-8') as file:
        json.dump(vocabulary, file, ensure_ascii=False, indent=4)
    print("Vocabulary saved to file.\n")

def load_vocabulary(filename):
    if os.path.exists(filename):
        with open(filename, 'r',encoding='utf-8') as file:
            return json.load(file)
    else:
        return {}

def show_current_vocabulary(vocabulary):
    print(f"Currently, you have {len(vocabulary)} words in your vocabulary.")
    
    for word, definition in vocabulary.items():
        print("-----------------------------------")
        print(f"{word}: {definition}")

def main():
    language_options = {
        '1': 'english',
        '2': 'ไทย',
        '3': '한국'
    }

    print("Choose language:")
    print("1. English")
    print("2. ไทย")
    print("3. 한국")
    language_choice = input("Enter language option (1/2/3): ").strip()

    if language_choice in language_options:
        language = language_options[language_choice]
        filename = f'vocabulary_{language}.json'
    else:
        print("Invalid language option. Defaulting to English.")
        language = 'english'
        filename = 'vocabulary_english.json'

    vocabulary = load_vocabulary(filename)

    while True:
        print("-----------------------------------")
        print(f"Vocabulary Application ({language})")
        print("1. Add new word")
        print("2. Practice vocabulary")
        print("3. Play game")
        print("4. Save vocabulary")
        print("5. Show current vocabulary")
        print("Enter 'e' to exit")
        print("-----------------------------------")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_word(vocabulary)
        elif choice == '2':
            practice_vocabulary(vocabulary)
        elif choice == '3':
            word_game_round(vocabulary)
        elif choice == '4':
            save_vocabulary(vocabulary, filename)
        elif choice == '5':
            show_current_vocabulary(vocabulary)
        elif choice.lower() == 'e':
            save_vocabulary(vocabulary, filename)
            print("-----------------------------------")
            print("Exiting the application.")
            print("-----------------------------------")
            break
        else:
            print("-----------------------------------")
            print("Invalid choice. Please choose again.\n")
            print("-----------------------------------")

if __name__ == "__main__":
    main()
