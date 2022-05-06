import random

loop_game = True

while loop_game is True:
    with open("hangman_words") as f:
        words = f.read().split()

    word = random.choice(words)
    correct_guesses = set()
    wrong_guesses = set()
    max_guesses = 8

    def guesses_remaining():
        return max_guesses - len(wrong_guesses)

    def has_won():
        return all(letter in correct_guesses for letter in word)

    def has_lost():
        return guesses_remaining() == 0


    while not has_won() and not has_lost():
        print("".join(letter if letter in correct_guesses else "-" for letter in word))
        print("{} guess remaining".format(guesses_remaining()))
        letter = input("Enter A Letter: ")
        if letter in word:
            correct_guesses.add(letter)
        elif len(letter) > 1:
            print("Too Many Letters")
        else:
            wrong_guesses.add(letter)


    print("Game over. The word was {}".format(word))
    start_over = input("Press Any Key To Continue or Press N To Stop Game: ").upper()
    if start_over == "N":
        loop_game = False
    else:
        loop_game = True