import random, sys
import urllib.request
import os.path

def random_string(a):
    str = ''
    for i in range(10):
        str += chr(random.randrange(65, 90))
    return "'" + str + "'"

def random_int(a):
    return random.randrange(-sys.maxsize, sys.maxsize)


def read_words_file():
    file_name = 'words.txt'

    if os.path.isfile(file_name):
        file = open(file_name, 'r')
        words = file.read().splitlines()
    else:
        word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
        response = urllib.request.urlopen(word_url)
        long_txt = response.read().decode()
        words = long_txt.splitlines()

        file = open(file_name, 'w')
        file.write(long_txt)

    return words

def random_words(a, word_dict_size=sys.maxsize, words=None):

    if words is None:
        words = read_words_file()

    word_dict_size = min(word_dict_size, len(words))

    str = ''
    for i in range(10):
        str += ' ' + words[random.randrange(0, word_dict_size)]
    return "'" + str[1:] + "'"