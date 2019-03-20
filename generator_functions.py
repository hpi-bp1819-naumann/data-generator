import random, sys
import urllib.request
import os.path


def random_string(a, previous_columns):
    str = ''
    for i in range(10):
        str += chr(random.randrange(65, 90))
    return "'" + str + "'"


def random_int(a, previous_columns):
    return random.randrange(-sys.maxsize, sys.maxsize)


def random_float(a, previous_columns, min=None, max=None):
    if max and min:
        return random.uniform(0, 1) * (max - min) + min
    return random.uniform(0, 1)


def random_boolean(a, previous_columns, weight_true=0.5):
    if random.uniform(0, 1) > weight_true:
        return 1
    else:
        return 0


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


def random_words(a, previous_columns, amount=10, word_dict_size=sys.maxsize, words=None):
    if words is None:
        words = read_words_file()

    word_dict_size = min(word_dict_size, len(words))

    str = ''
    for i in range(amount):
        str += ' ' + words[random.randrange(0, word_dict_size)]
    return "'" + str[1:] + "'"


def random_word(a, previous_column, word_dict_size=sys.maxsize, words=None):
    if words is None:
        words = read_words_file()

    word_dict_size = min(word_dict_size, len(words))
    return words[random.randrange(0, word_dict_size)]


def weight_dependent_on_cat(a, prev_col):
    if prev_col["category"] in ["\'abstruse\'",
                                "\'Abe\'",
                                "\'abridgment\'",
                                "\'Abram\'",
                                "\'Abernathy\'",
                                "\'abacus\'",
                                "\'Abelson\'",
                                "\'abbot\'",
                                "\'abdomen\'",
                                "\'AAA\'",
                                "\'abstention\'",
                                "\'aboriginal\'"]:
        return str(random_float(a,
                                prev_col,
                                min=30,
                                max=70))
    else:
        return str(random_float(a,
                                prev_col,
                                min=0.5,
                                max=40))


def boolean_dependent_on_weight(a, prev_col):
    if float(prev_col["weight"]) >= 30.0:
        prob = 0.75
    else:
        prob = 0.4
    return random.random() < prob


def conditonal_true(a, prev_col):
    if sum(float(i) for i in [prev_col["att1"], prev_col["att2"], prev_col["att3"], prev_col["att6"], prev_col["att7"], prev_col["att8"]]) > 3.0 or sum(float(i) for i in [prev_col["att1"], prev_col["att3"], prev_col["att7"]]) > 2.0 or (sum(float(i) for i in [prev_col["att2"], prev_col["att6"], prev_col["att8"]]) > 1.5 and prev_col["att4"] == "\'Y\'"):
        return str(True)
    else:
        return str(False)
