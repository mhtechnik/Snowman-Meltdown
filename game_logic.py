
"""Spiel-Logik für Snowman Meltdown.

Best Practices:
- PEP 8-konforme Namen und Zeilenlängen
- Typannotationen
- Klare, kleine Funktionen mit Single Responsibility
- Keine magischen Zahlen (Konstanten)
"""

from __future__ import annotations

import random
from typing import Set

from ascii_art import STAGES

# --- Konstanten -------------------------------------------------------------

WORDS: tuple[str, ...] = (
    "python",
    "git",
    "github",
    "snowman",
    "meltdown",
    "branch",
    "commit",
    "merge",
)
MAX_MISTAKES: int = len(STAGES) - 1


# --- Hilfsfunktionen --------------------------------------------------------

def get_random_word() -> str:
    """Return a random secret word from WORDS."""
    return random.choice(WORDS)


def display_game_state(
    mistakes: int,
    secret_word: str,
    guessed_letters: Set[str],
) -> None:
    """Print current ASCII-art stage and word progress."""
    stage_index = min(mistakes, MAX_MISTAKES)

    print("\n" + "=" * 40)
    print(STAGES[stage_index])
    print("-" * 40)

    display_word = " ".join(
        ch if ch in guessed_letters else "_" for ch in secret_word
    )
    print(f"Word:      {display_word}")
    print(f"Mistakes:  {mistakes}/{MAX_MISTAKES}")

    tried = " ".join(sorted(guessed_letters)) if guessed_letters else "-"
    print(f"Guessed:   {tried}")
    print("=" * 40 + "\n")


def is_word_guessed(secret_word: str, guessed_letters: Set[str]) -> bool:
    """Return True if all letters in secret_word are in guessed_letters."""
    # set() vermeidet doppelte Buchstaben im Check
    return all(ch in guessed_letters for ch in set(secret_word))


def prompt_letter() -> str:
    """Prompt for exactly one alphabetical character (a–z)."""
    while True:
        raw = input("Guess a letter [a-z]: ").strip().lower()

        if len(raw) != 1:
            print("Bitte genau EIN Zeichen eingeben.")
            continue

        if not raw.isalpha():
            print("Bitte nur Buchstaben (a–z) eingeben.")
            continue

        return raw


def prompt_yes_no(msg: str = "Play again? [y/n]: ") -> bool:
    """Prompt a yes/no question. Return True for yes, False for no."""
    while True:
        ans = input(msg).strip().lower()

        if ans in {"y", "yes", "j", "ja"}:
            return True
        if ans in {"n", "no", "nein"}:
            return False

        print("Bitte mit 'y'/'yes'/'j' oder 'n'/'no' antworten.")


# --- Runden- und Hauptspiel -------------------------------------------------

def play_round() -> bool:
    """Play a single round. Return True if won, else False."""
    secret_word = get_random_word()
    guessed_letters: Set[str] = set()
    mistakes = 0

    print("\nWelcome to Snowman Meltdown!")
    # Debug bei Bedarf:
    # print(f"[DEBUG] secret: {secret_word}")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        if is_word_guessed(secret_word, guessed_letters):
            print(f"🎉 Gerettet! Das Wort war: {secret_word}\n")
            return True

        if mistakes >= MAX_MISTAKES:
            print(
                f"💧 Verloren! Der Schneemann ist geschmolzen. "
                f"Wort: {secret_word}\n"
            )
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


def play_game() -> None:
    """Main loop with replay option."""
    while True:
        play_round()
        if not prompt_yes_no("Noch einmal spielen? [y/n]: "):
            print("Danke fürs Spielen! Bis zum nächsten Mal.")
            break


# --- Entry Point ------------------------------------------------------------

if __name__ == "__main__":
    play_game()
