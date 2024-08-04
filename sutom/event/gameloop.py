from datetime import datetime
from sutom.config.parser_const import DEBUG, DEBUG_FILE
from sutom.debug.debug_tools import print_console_log
from sutom.event.word import compare

NB_TRY = 6


def without_timeout(word: str) -> int:
    """
    The main loop without the time mode.
    Args:
        word: str, the chosen word by the game.

    Returns:
        int, the number of tries that the player took before guessing the word.
    """
    nb_trial = 0
    hidden_word = _masking_word(word)
    size = len(hidden_word)
    print_console_log("In {} letters :".format(size), on_console=True)
    while nb_trial != NB_TRY:
        print_console_log(hidden_word, on_console=True)
        given_string = input("Type a word : ").lower()
        print_console_log("The player has typed " + given_string, on_log=DEBUG, debug_file=DEBUG_FILE)
        if len(given_string) != size:
            print_console_log("Please, the given word should be the same size "
                              + "({} letters) as the random word !".format(size), on_console=True)
            continue
        if given_string[0] != word[0]:
            print_console_log("Should start with the same letter", on_console=True)
            continue
        if given_string == word:
            return nb_trial
        hidden_word = compare(word, given_string)
        nb_trial += 1
    return -1


def _masking_word(word: str):
    """
    Replaces every character (except the first) by a dot.
    Args:
        word: str, the word we want to mask.

    Returns:
        str, the word that has been masked.
    """
    hidden_word = word[0]
    size = len(word)
    for i in range(1, size):
        if word[i] == "-":
            hidden_word += "-"
        else:
            hidden_word += "."
    return hidden_word
