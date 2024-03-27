import argparse
from dotenv import dotenv_values
from app import timecard

if __name__=='__main__':

    # example
    # {"COMPANY": "company", "USERNAME": "username", "PASSWORD": "password"}
    config = dotenv_values(".env")

    argParser = argparse.ArgumentParser(
            prog = 'timecard',
            description = 'springahead auto timecard entry',
            epilog = 'thanks for playing')

    argParser.add_argument("-c", "--copy", help="copy last week")
    argParser.add_argument("-d", "--date", help="a date within the specified week")
    argParser.add_argument("-H", "--hours", help="hours for the past week")

    args = argParser.parse_args()

    timecard.run(config, args)
