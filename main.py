import json
import os
import random

def word_game_round(vocabulary):
    if not vocabulary:
        print("No words in the dictionary. Add some words first!\n")
        return
    print("-----------------------------------")
    print('How many round do you prefer to play? (At least should be 10 round)')
    while True:
        try:   
            g_round = input('Enter number of round: ').strip()
            g_round_int = int(g_round)
            if g_round_int < 10:
                print('The number of rounds should be at least 10.')
                continue
            break
        except ValueError:
            print('Invalid input, The input should be number.')
            
    point = 0
    
    for i in range(g_round_int):
        word, definition = random.choice(list(vocabulary.items()))
        print("-----------------------------------")
        print(f'round {i+1}')
        print(f"What's definition of {word}")
        user_ans = input('The definition is: ').strip()
        
        if user_ans.lower() == definition.lower():
            print('Good job!!\n')
            print("-----------------------------------")
            point+=1
        else:
            print(f"Incorrect! The correct definition is {definition}.\n")
            print("-----------------------------------")
    print("-----------------------------------")
    print(f"Finish the game you got {point}/{g_round_int}")

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
    print(f"What is this word mean: {word}")
    print("-----------------------------------")
    user_answer = input("What's the definition ").strip()

    if user_answer.lower() == definition.lower():
        print("-----------------------------------")
        print("Correct!\n")
        print("-----------------------------------")
    else:
        print("-----------------------------------")
        print(f"Incorrect! This {word} mean '{definition}'.\n")
        print("-----------------------------------")

def save_vocabulary(vocabulary, filename='vocabulary.json'):
    with open(filename, 'w') as file:
        json.dump(vocabulary, file)
    print("Vocabulary saved to file.\n")

def load_vocabulary(filename='vocabulary.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        return {}
def show_current_Volcabulary(vocabulary):
    print(f"Currently you have {len(vocabulary)}")
    
    for w,d in vocabulary.items():
        print("-----------------------------------")
        print(f"{w} that mean: {d}")

def main():
    vocabulary = load_vocabulary()
    while True:
        print("-----------------------------------")
        print("Vocabulary Application")
        print("1. Add new word")
        print("2. Practice vocabulary")
        print("3. Playing game")
        print("4. Save vocabulary")
        print('5. Show current vocabulary')
        print('Enter e to exit')
        print("-----------------------------------")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_word(vocabulary)
        elif choice == '2':
            practice_vocabulary(vocabulary)
        elif choice == '3':
            word_game_round(vocabulary)
        elif choice == '4':
            save_vocabulary(vocabulary)
        elif choice == '5':
            show_current_Volcabulary(vocabulary)
        elif choice == 'e':
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