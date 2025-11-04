import random

# ===== Snowman ASCII Art stages =====
STAGES = [
    # Stage 0: Full snowman
    """
     ___  
    /___\\ 
    (o o) 
    ( : ) 
    ( : ) 
    """,
    # Stage 1: Bottom part starts melting
    """
     ___  
    /___\\ 
    (o o) 
    ( : ) 
    """,
    # Stage 2: Only the head remains
    """
     ___  
    /___\\ 
    (o o) 
    """,
    # Stage 3: Snowman completely melted
    """
     ___  
    /___\\ 
    """
]

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Zeigt die ASCII-Art-Phase und das aktuelle Wort (mit Unterstrichen)."""
    # Safety: stelle sicher, dass der Index im Bereich liegt
    stage_index = min(mistakes, len(STAGES) - 1)
    print(STAGES[stage_index])

    # Wort mit Unterstrichen bzw. aufgedeckten Buchstaben darstellen
    display_word = []
    for letter in secret_word:
        display_word.append(letter if letter in guessed_letters else "_")
    print("Word:", " ".join(display_word))
    print(f"Mistakes: {mistakes}\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
   

    # Initialen Zustand anzeigen (Phase 0, alles Unterstriche)
    display_game_state(mistakes, secret_word, guessed_letters)

    
    guess = input("Guess a letter: ").lower().strip()
    print("You guessed:", guess)

   

if __name__ == "__main__":
    play_game()
