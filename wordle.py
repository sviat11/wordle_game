import random




words_array = []

RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
WHITE = "\033[1;37m"


def color_print(color_code, *args):
    print(color_code)
    print(*args)
    print(WHITE)


text_file = open("text.txt").read().splitlines()
random_word = random.choice(text_file)
random_word = random_word.upper()

for letter in random_word:
    words_array.append(letter)




def wordle():
    print(words_array)
    attempts = 0
    keep_going = True
    while keep_going:
        user_input = input("Enter your word: ").upper()

        if len(user_input) < 5 or len(user_input) > 5:
            print("Your length is too short! please enter the correct value: ")
            continue

        user_guess = [*user_input]
        output = ""

        for i in range(len(user_guess)):
            if user_guess[i] == words_array[i]:
                color = GREEN
                character = user_guess[i]
            elif user_guess[i] in words_array:
                color = YELLOW
                character = user_guess[i]
            else:
                color = RED
                character = user_guess[i]
            output += color + character + " "
        output += WHITE
        print(output)
        attempts += 1

        if user_guess == words_array:
            color_print(GREEN, "You guessed! Well done")
            keep_going = False

        elif attempts == 5:
            color_print(RED, "You have run out of attempts")
            keep_going = False

        print("\n")

wordle()
print("Do you want to play wordle? (y/n)")
user_input = input("y / n: ")
if user_input == "y":
    wordle()
else:
    print(GREEN + "Thank you for playing")
