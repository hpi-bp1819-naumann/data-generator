import random

import DataGenCSV
import generator_functions

host = 'localhost'
user = 'justus'
password = 'Sparschwein-Bild'
db_name = 'shifts'
table_name = 'prior_prob_att1_p1'
entries = 50000

function_list = {
    "idx": {"sql_type": "INTEGER", "function": lambda a, prev_col: str(a)},
    "name": {"sql_type": "TEXT", "function": generator_functions.random_string},
    "att1": {"sql_type": "FLOAT", "function":
        lambda a, prev_col: str(generator_functions.random_float(a, prev_col))},
    "att2": {"sql_type": "FLOAT", "function":
        lambda a, prev_col: str(generator_functions.random_float(a, prev_col))},
    "att3": {"sql_type": "FLOAT", "function":
        lambda a, prev_col: str(generator_functions.random_float(a, prev_col))},
    "att4": {"sql_type": "TEXT", "function":
        lambda a, prev_col: random.choice(["\'Y\'", "\'\'"])},
    "att5": {"sql_type": "BOOLEAN", "function":
        lambda a, prev_col: str(True) if float(prev_col["att2"]) > 0.5 else str(False)},
    "att6": {"sql_type": "FLOAT", "function":
        lambda a, prev_col: str(generator_functions.random_float(a, prev_col))},
    "att7": {"sql_type": "FLOAT", "function":
        lambda a, prev_col: str(generator_functions.random_float(a, prev_col))},
    "att8": {"sql_type": "FLOAT", "function":
        lambda a, prev_col: str(generator_functions.random_float(a, prev_col))},
    "att9": {"sql_type": "BOOLEAN", "function":
        lambda a, prev_col: generator_functions.conditonal_true(a, prev_col)}
}

with DataGenCSV.DataGenerator(file_name="prior_prob_att9_p1.csv") as gen:
    gen.generate_data(function_list, entries)
