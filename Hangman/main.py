def print_current_state(letters_guessed, letters_tried, lives):
    if not lives == 0:
        print(" ".join(letters_guessed), end="      ")
        print(f"Letters tried: {' '.join(letters_tried)}")
        print(f"Lives left: {lives}")


lives = 10
guess = False
letters_tried = set()
word_to_guess = input().lower()

letters_guessed = len(word_to_guess) * ["_"]
print_current_state(letters_guessed, letters_tried, lives)

while "_" in letters_guessed and not lives == 0:
    print("Try another letter")
    letter = input().lower()
    for index in range(len(word_to_guess)):
        if word_to_guess[index] == letter:
            letters_guessed[index] = letter
            guess = True
    if guess == False:
        letters_tried.add(letter)
        lives -= 1
    print_current_state(letters_guessed, letters_tried, lives)
    guess = False

if not lives == 0:
    print("You win!")
else:
    print(f"You died. Word was {''.join(word_to_guess)}")