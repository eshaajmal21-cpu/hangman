import random

fruits = ["apple", "banana", "orange", "grape", "strawberry"]

guess = random.choice(fruits)
length = len(guess)

display = ["-"] * length
lives = 6
guessed_letters = set()

print("Word:", " ".join(display))

while "-" in display and lives > 0:
    x = input("Guess a letter: ").lower()

    # Check if input is valid
    if len(x) != 1 or not x.isalpha():
        print("Please enter a single alphabet.")
        continue

    # Check if already guessed
    if x in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(x)

    # Check if letter is in the word
    if x in guess:
        for i in range(length):
            if guess[i] == x:
                display[i] = x
        print("Correct!")
    else:
        lives -= 1
        print("Incorrect!")
        print(f"You lost 1 life. Remaining lives: {lives}")

    print("Word:", " ".join(display))

# Final result
if "-" not in display:
    print("\n🎉 You win the game!")
else:
    print(f"\n❌ You lose the game. The correct word was '{guess}'.")