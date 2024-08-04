from .parser import create_parser

ARGS = create_parser()
DEBUG = True if ARGS.debug is not None else False
DEBUG_FILE = ARGS.debug[0] if ARGS.debug is not None else ""
