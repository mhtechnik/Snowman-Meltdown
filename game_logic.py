
import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Zeigt ASCII-Art-Phase, aktuelles Wort (Unterstriche) und Status."""
    stage_index = min(mistakes, len(STAGES) - 1)
    print(STAGES[stage_index])

    display_word = []
    for letter in secret_word:
        display_word.append(letter if letter in guessed_letters else "_")

    print("Word:     ", " ".join(display_word))
    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}")
    print(f"Guessed:  {' '.join(sorted(guessed_letters)) if guessed_letters else '-'}\n")


def is_word_guessed(secret_word, guessed_letters):
    """True, wenn alle Buchstaben des geheimen Wortes geraten wurden."""
    return all(ch in guessed_letters for ch in set(secret_word))


def play_game():
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    
    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        
        if is_word_guessed(secret_word, guessed_letters):
            print("🎉 Du hast den Schneemann gerettet! Das Wort war:", secret_word)
            break
        if mistakes >= max_mistakes:
            print("💧 Der Schneemann ist geschmolzen! Das Wort war:", secret_word)
            break

        
        guess = input("Guess a letter: ").lower().strip()

        
        if not guess or len(guess) != 1 or not guess.isalpha():
            print("Bitte genau einen Buchstaben (a–z) eingeben.\n")
            continue
        if guess in guessed_letters:
            print("Diesen Buchstaben hast du schon versucht.\n")
            continue

        
        if guess in secret_word:
            guessed_letters.add(guess)
            print(f"Gut geraten! '{guess}' ist im Wort.\n")
        else:
            mistakes += 1
            print(f"Leider falsch. '{guess}' kommt nicht vor.\n")


if __name__ == "__main__":
    play_game()
