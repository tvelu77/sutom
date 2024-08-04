from datetime import datetime


def print_console_log(message: str, on_console: bool = False, on_log: bool = False, debug_file: str = None):
    """
    Prints the message in the console or in the log (or both !).
    Args:
        on_console: bool, should we print in the console.
        on_log: bool, should we print in the log.
        debug_file: str, the file's path.
        message: str, the message we want to print.
    """
    if on_console:
        print(message)
    if on_log and debug_file is not None:
        _write_log(debug_file, message)


def _write_log(debug_file: str, message: str):
    """Writes in the user's defined file if the debug option is on.

    Args:
        debug_file: debug file's path.
        message: the message that will be written in the file.

    Raises:
        ValueError: if the file couldn't be created.
    """
    now = datetime.now()
    current_time = now.strftime("%d/%m/%y - %H:%M:%S")
    try:
        with open(debug_file, 'a') as fd:
            fd.write(current_time + " DEBUG: " + message + "\n")
    except FileNotFoundError:
        raise ValueError("the file \"{}\" couldn't be created, please retry using another name"
                         .format(debug_file))

