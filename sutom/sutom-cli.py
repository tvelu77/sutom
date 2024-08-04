from time import time
from sys import maxsize

from debug.debug_tools import print_console_log
from config.parser_const import ARGS, DEBUG, DEBUG_FILE
from event.gameloop import without_timeout
from sutom.event.word import initialize_word, initialize_words_array

NB_TRY = 6


def victory(nb_of_try: int):
    """Shows a message to alert the player that he has won.

    Args:
        nb_of_try (int): the number of try that the player
        took to guess the word.
    """
    nb_of_try += 1
    correct_suffix = "th"
    if nb_of_try == 1:
        correct_suffix = "st"
    elif nb_of_try == 2:
        correct_suffix = "nd"
    elif nb_of_try == 3:
        correct_suffix = "rd"
    print("Congratulations, you won on the {}{} try !"
          .format(nb_of_try, correct_suffix))


def gameloop(gameword: str) -> int:
    """The gameloop.
    What it does :

    - Infinite looping until the word has been found,
    or if the user is out of try.

    - Compare the string given by the user to the random word.

    - If it's the correct word, then the user has won.

    - If it's not correct, then the program will tell the user
    if the letters that has been correctly/incorrectly placed.

    Args:
        gameword (str): the random word choosen from the tsv file.

    Returns:
        int: the number of try, or -1 if the player lose the game.
    """
    return without_timeout(gameword)


def _get_limit() -> tuple[int, int]:
    if ARGS.min:
        min_value = ARGS.min[0]
        if min_value < 0:
            print_console_log("min \"{}\" value is negative, setting to 0...".format(min_value),
                              on_console=True,
                              on_log=DEBUG,
                              debug_file=DEBUG_FILE)
            min_value = 0
    else:
        min_value = 0
    if ARGS.max:
        max_value = ARGS.max[0]
        if max_value < min_value or max_value <= 1:
            print_console_log("max \"{}\" is inferior to min \"{}\", removing max...".format(max_value, min_value),
                              on_console=True,
                              on_log=DEBUG,
                              debug_file=DEBUG_FILE)
            max_value = maxsize
    else:
        max_value = maxsize
    return min_value, max_value


def main():
    """The main function used to call all the function.
    For example, generate a new word and launching the gameloop.
    """
    print_console_log("Loading, please wait...", on_console=True)
    chosen_seed = int(time())
    if ARGS.seed:
        chosen_seed = ARGS.seed[0]
    print_console_log("The chosen seed is {}".format(chosen_seed),
                      on_console=True,
                      on_log=DEBUG,
                      debug_file=DEBUG_FILE)
    min_value, max_value = _get_limit()
    words_array = initialize_words_array(min_value, max_value)
    if ARGS.target:
        gameword = ARGS.target[0].strip()
        if len(gameword) <= 1:
            print_console_log("The target word \"{}\" is not a correct word ,"
                              + "choosing a random word...".format(gameword),
                              on_console=True,
                              on_log=DEBUG,
                              debug_file=DEBUG_FILE)
            gameword = initialize_word(chosen_seed, words_array)
    else:
        gameword = initialize_word(chosen_seed, words_array)
    print_console_log("The chosen word is {}".format(gameword), on_log=DEBUG, debug_file=DEBUG_FILE)
    has_won = gameloop(gameword)
    if has_won == -1:
        print_console_log("The player lost the game\nThe word was \"{}\"".format(gameword),
                          on_console=True,
                          on_log=DEBUG,
                          debug_file=DEBUG_FILE)
    else:
        print_console_log("The player has won after {} tries"
                          .format(has_won), on_log=DEBUG, debug_file=DEBUG_FILE)
        victory(has_won)


if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        error = "An error has occurred, please check the game file ! For more information : {}".format(e)
        print_console_log(error, on_console=True, on_log=DEBUG, debug_file=DEBUG_FILE)
