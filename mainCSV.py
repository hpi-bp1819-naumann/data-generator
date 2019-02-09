import DataGenCSV
import generator_functions

entries = 10000

function_list = {
    "idx": {"sql_type": "INTEGER", "function": lambda a: str(a)},
    "square": {"sql_type": "BIGINT", "function": lambda a: str(a*a)},
    "random_string": {"sql_type": "TEXT", "function": generator_functions.random_string}
}

with DataGenCSV.DataGenerator(file_name='data.csv') as gen:
    gen.generate_data(function_list, entries)
