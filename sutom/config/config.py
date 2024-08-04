from _csv import reader


def check_config_file(file: str = "config/config.txt") -> dict[str, str]:
    """Reads a config file and returns a dictionary containing all the config file info.

    Args:
        file (str): the config file's path (Default: config.txt).

    Returns:
        dict[str, str]: key(the parameter name), value(the parameter value).

    """
    config_dictionary = dict()
    try:
        with open(file, 'r') as fd:
            rd = reader(fd, delimiter="\n")
            for row in rd:
                if len(row) == 0:
                    continue
                if row[0].startswith("#"):
                    continue
                if "=" not in row[0]:
                    continue
                parameter = row[0].split("=", 3)
                config_dictionary[parameter[0].strip()] = parameter[1].strip()
        return config_dictionary
    except FileNotFoundError:
        raise ValueError("cannot find {} config file !".format(file))
