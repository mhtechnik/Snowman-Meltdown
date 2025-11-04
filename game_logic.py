
import random
from ascii_art import STAGES


WORDS = ["python", "git", "github", "snowman", "meltdown", "branch", "commit", "merge"]

MAX_MISTAKES = len(STAGES) - 1


def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Zeigt ASCII-Art, Wortanzeige, Fehlerstand und bereits geratene Buchstaben."""
    stage_index = min(mistakes, MAX_MISTAKES)
    print("\n" + "=" * 40)
    print(STAGES[stage_index])
    print("-" * 40)

    
    display_word = " ".join([ch if ch in guessed_letters else "_" for ch in secret_word])
    print(f"Word:      {display_word}")
    print(f"Mistakes:  {mistakes}/{MAX_MISTAKES}")

    if guessed_letters:
        tried = " ".join(sorted(guessed_letters))
    else:
        tried = "-"
    print(f"Guessed:   {tried}")
    print("=" * 40 + "\n")


def is_word_guessed(secret_word, guessed_letters):
    """True, wenn alle Buchstaben des Wortes geraten sind."""
    return all(ch in guessed_letters for ch in set(secret_word))


def prompt_letter():
    """
    Fragt den Nutzer nach genau einem alphabetischen Buchstaben (a–z).
    Wiederholt, bis Eingabe gültig ist.
    """
    while True:
        raw = input("Guess a letter [a-z]: ").strip().lower()
        if len(raw) != 1:
            print("Bitte genau EIN Zeichen eingeben.")
            continue
        if not raw.isalpha():
            print("Bitte nur Buchstaben (a–z) eingeben.")
            continue
        return raw


def prompt_yes_no(msg="Play again? [y/n]: "):
    """Fragt y/n ab, liefert True für ja, False für nein."""
    while True:
        ans = input(msg).strip().lower()
        if ans in ("y", "yes", "j", "ja"):
            return True
        if ans in ("n", "no", "nein"):
            return False
        print("Bitte mit 'y'/'yes'/'j' oder 'n'/'no' antworten.")


def play_round():
    """Spielt eine einzelne Runde. Gibt True zurück, wenn gewonnen, sonst False."""
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0

    print("\nWelcome to Snowman Meltdown!")
    

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        
        if is_word_guessed(secret_word, guessed_letters):
            print(f"🎉 Gerettet! Das Wort war: {secret_word}\n")
            return True
        if mistakes >= MAX_MISTAKES:
            print(f"💧 Verloren! Der Schneemann ist geschmolzen. Wort: {secret_word}\n")
            return False

        
        guess = prompt_letter()

        if guess in guessed_letters:
            print("Hinweis: Buchstaben bereits versucht.\n")
            continue

        guessed_letters.add(guess)
        if guess in secret_word:
            print(f"Gut geraten! '{guess}' ist im Wort.\n")
        else:
            mistakes += 1
            print(f"Leider falsch. '{guess}' kommt nicht vor. (+1 Fehler)\n")


def play_game():
    """Hauptschleife mit Wiederholen-Option."""
    while True:
        play_round()
        if not prompt_yes_no("Noch einmal spielen? [y/n]: "):
            print("Danke fürs Spielen! Bis zum nächsten Mal.")
            break


if __name__ == "__main__":
    play_game()
