import random
def play_game():
    print("--Get ready to play Hangman Game--")
    categories = {
        "fruits": ["apple", "banana", "mango", "orange", "grape"],
        "countries": ["india", "america", "brazil", "canada", "france"],
        "colors": ["red", "blue", "green", "yellow", "purple"],
        "animals": ["tiger", "elephant", "dog", "cat", "lion"],
        "flowers": ["rose", "lily", "tulip", "jasmine", "orchid"]
    }
    print("Choose a category: fruits, countries, colors, animals, flowers")
    category = input("Your choice: ").lower()
    if category not in categories:
        print("Please choose the correct category!")
        category = "fruits"
    word = random.choice(categories[category])
    guessed = []
    for _ in word:
        guessed.append("_")
    attempts = 6
    used_letters = set()
    clue_count = 2  
    clue_positions = random.sample(range(len(word)), clue_count)
    for pos in clue_positions:
        guessed[pos] = word[pos]
        used_letters.add(word[pos])
    while attempts > 0 and "_" in guessed:
        print("\nWord: ", " ".join(guessed))
        print("Used letters:", " ".join((used_letters)))
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue
        used_letters.add(guess)
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print(f"Incorrect! {attempts} attempts left.")
    if "_" not in guessed:
        print("\nCongrats! You found the word:", word)
    else:
        print("\nOh no!! Game over! The word was:", word)
while True:
    play_game()
    retry = input("\nDo you want to try again? (y/n): ").lower()
    if retry != 'y':
        print("See you soon :)")
        break
