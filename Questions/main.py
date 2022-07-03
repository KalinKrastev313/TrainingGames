import random
# length = 1000
# with open("database_en_easy.txt", encoding="utf8") as file:
#     length = len(file.readlines())


def first_view_answer(answer, guess_progress):
    for char in answer:
        if char.isalpha():
            guess_progress.append("_")
        else:
            guess_progress.append(char)
    return " ".join(guess_progress)


def check_if_guess_is_right(letter, answer, guess_progress):
    guess_is_right = False
    for index in range(len(answer)):
        if letter == answer[index]:
            guess_progress[index] = letter
            guess_is_right = True
    return guess_is_right


def single_question(lives):
    with open(chosen_database, encoding="utf8") as file:
        data = file.readlines()
        length = len(data)
        text = data[random.randint(0, length)]

    letters_tried = []
    question, answer = text.split("?")

    guess_progress = []

    print(f"{question}?")
    print(first_view_answer(answer, guess_progress))
    while "_" in guess_progress and lives > 0:
        letter = input().upper()
        if not letter in letters_tried:
            if letter.isalpha():
                letters_tried.append(letter)
            else:
                print("This is not a letter!")
                continue
        else:
            print("You already tried this letter!")
            continue
        guess_is_right = check_if_guess_is_right(letter, answer, guess_progress)
        if not guess_is_right:
            lives -= 1

        print(" ".join(guess_progress))
        print(f"Lives left: {lives}       Letters tried:{', '.join(letters_tried)}")

    return lives, answer


print("Choose language for the questions: 1-BG , 2-EN")
language = int(input())
if language == 1:   # Bulgarian
    chosen_database = "database_bg.txt"
elif language == 2:     # English
    print("Choose difficulty: 1-Easy , 2-Hard")
    difficulty = int(input())
    if difficulty == 1:     # Easy
        chosen_database = "database_en_easy.txt"
    else:
        chosen_database = "database_en_hard.txt"

lives = 10
regen_per_question = 3

while True:
    lives, answer = single_question(lives)
    if lives == 0:
        print(f"You died! The word was {answer}")
        break
    else:
        print("You guessed right!")
        lives += regen_per_question
    print("Would you like another question? Y or N")
    persist = input().upper()
    if persist == "N":
        break



