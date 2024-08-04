from argparse import ArgumentParser, Namespace


def create_parser() -> Namespace:
    """Creates a parser and adds rules for the user.

    Returns the arguments given by the user.

    debug option : writes in a log file every event that happened during the execution.

    MORE OPTIONS ARE EXPECTED TO BE ADDED.

    Returns:
        Namespace: the arguments that has been given by the user.

    """
    parser = ArgumentParser(description="SUTOM\nGuess the random word !")
    parser.add_argument('--debug', metavar="FILE'S PATH", dest='debug', type=str, nargs=1,
                        help='activate the debug mode and write in the given file')
    parser.add_argument('--target', '-t', metavar="WORD", dest='target', type=str, nargs=1,
                        help='set the random word')
    parser.add_argument('--seed', metavar="SEED", dest='seed', type=int, nargs=1,
                        help='set the seed for the random word')
    parser.add_argument('--min', metavar='MIN', dest='min', nargs=1, type=int,
                        help='define the minimum of characters that a word can have')
    parser.add_argument('--max', metavar='MAX', dest='max', nargs=1, type=int,
                        help='define the maximum of characters that a word can have')
    parser.add_argument('--time-mode', dest='timeout', action='store_true',
                        help='activate the time mode (60 seconds by default)')
    return parser.parse_args()
