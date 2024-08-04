from _csv import reader
from random import seed, randint
from sys import maxsize

from sutom.config.config_const import CONFIG_DICTIONARY
from sutom.config.parser_const import DEBUG, DEBUG_FILE
from sutom.debug.debug_tools import print_console_log


def compare(game_string: str, user_string: str) -> str:
    """
    Compares the given string to the chosen string,
    and returns a string showing the correct/incorrect
    characters placements.

    Args:
        game_string (str): chosen string by the game.
        user_string: user's given string.

    Returns:
        str: string showing the correct character.

    """
    result = []
    letters_left_user = []
    letters_left_game = []
    for i in range(len(game_string)):
        if game_string[i] == user_string[i]:
            letters_left_user.append(None)
            letters_left_game.append(None)
            result.append(user_string[i])
        else:
            letters_left_user.append(user_string[i])
            letters_left_game.append(game_string[i])
            result.append(".")
    for i in range(len(letters_left_user)):
        letter = letters_left_user[i]
        if result[i] != ".":
            continue
        if letter in letters_left_game:
            result[i] = "~"
            for j in range(len(letters_left_game)):
                if letter == letters_left_game[j]:
                    letters_left_game[j] = None
                    break
    return "".join(result)


def initialize_words_array(min_value: int = 0, max_value: int = maxsize) -> list[str]:
    """
    Initializes the array containing words respecting the limits.
    Args:
        min_value: int, the minimum length of a word.
        max_value: int, the maximum length of a word.

    Returns:
        list[str], list containing all the words.
    """
    array = []
    fallback_array = []
    try:
        with open(CONFIG_DICTIONARY["WORDS_FILE"], "r") as fd:
            rd = reader(fd, delimiter="\t", quotechar='"')
            for row in rd:
                if min_value <= len(row[0]) <= max_value:
                    array.append(row[0])
                fallback_array.append(row[0])
    except FileNotFoundError:
        raise ValueError("{} is not existent, "
                         + "please check the file"
                         .format(CONFIG_DICTIONARY["WORDS_FILE"]))
    if len(array) == 0:
        if len(fallback_array) == 0:
            raise ValueError("The file \"{}\" is not correctly formatted".format(CONFIG_DICTIONARY["WORDS_FILE"]))
        print_console_log("The limit min = {} given is wrong".format(min_value, max_value) +
                          ", no words could be found\nChoosing a random word...",
                          on_console=True,
                          on_log=DEBUG,
                          debug_file=DEBUG_FILE)
        return fallback_array
    return array


def initialize_word(chosen_seed: int, array: list[str]) -> str:
    """
    Returns a random word from the given array.
    Returns:
        str: a random word.
    """
    seed(chosen_seed)
    random_int = randint(0, len(array))
    return array[random_int]
