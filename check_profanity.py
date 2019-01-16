from urllib.request import urlopen
from urllib.parse import quote


def read_text():
    with open("/Users/dcasanova/PycharmProjects/ProgrammingFoundations/movie_quotes.txt") as quotes:
        contents_of_file = quotes.read()
        # print(contents_of_file)
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    url_query = quote(text_to_check)
    with urlopen('http://www.wdylike.appspot.com/?q=' + url_query) as connection:
        output = str(connection.read())
    if 'true' in output:
        print("Profanity Alert!!")
    elif 'false' in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")


read_text()
