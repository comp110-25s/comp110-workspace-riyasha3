"""Creating a Wordle Game."""

__author__: str = "730519187"


def contains_char(word: str, letter: str) -> bool:
    """Finds if any of the letters match the letters in the word."""
    assert len(letter) == 1, f"len('{letter}')is not 1"

    index: int = 0
    while index < len(word):
        if word[index] == letter:
            return True
        index += 1
    return False  # Characters at the index are not the same


def emojified(
    guess: str, secret_word: str
) -> (
    str
):  # This function gave me a hard time and it took a while to fix in office hours.
    """Returns different colored emoji depending on if letter match."""
    assert len(guess) == len(secret_word), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    idx: int = 0
    outp = ""  # It allows the emojis to add on as the while loop continues.
    while idx < len(guess):
        if guess[idx] == secret_word[idx]:
            outp += GREEN_BOX
        elif contains_char(secret_word, guess[idx]):
            outp += YELLOW_BOX
        else:
            outp += WHITE_BOX
        idx += 1
    return outp


def input_guess(N: int) -> str:
    """Makes sure that the correct length of word is guessed."""
    guess = input(f"Enter a {N} character word: ")  # Works on any number of letters!
    while len(guess) != N:
        guess = input(f"That wasn't {N} chars!")
    return guess


def main(secret: str) -> None:  # Nothing is returned.
    """The entrypoint of the program and main game loop."""

    turn: int = 1
    max_turn: int = 7
    is_won = False

    while (
        turn < max_turn
        and not is_won  # Makes sure game stops once the correct word is guessed.
    ):  # Loops until the guesser goes through 6 turns.
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(N=len(secret))
        print(
            emojified(guess, secret)
        )  # Can't just call the emojified function. Need to print it.
        if guess == secret:
            print(f"You won in {turn}/6 turns!")  # Yay!
            is_won = True
        else:
            turn += 1

    if not is_won or turn > max_turn:
        print("X/6 - Sorry, try again tomorrow!")  # Boo :(


if __name__ == "__main__":
    main(secret="codes")
# Yay! I can code wordle now!
