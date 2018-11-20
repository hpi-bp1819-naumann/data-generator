import DataGen
import generator_functions

host = 'localhost'
user = 'dbuser'
password = 'password'
db_name = 'testdb_2'
table_name = 'myTable'
entries = 1000

function_list = {
        "idx" : {"sql_type" : "INTEGER", "function" : lambda a : str(a)},
        "square" : {"sql_type" : "BIGINT", "function" : lambda a : str(a*a)},
        "random_string" : {"sql_type" : "TEXT", "function" : generator_functions.random_string}
        }

with DataGen.DataGenerator(host=host, user=user, password=password, db_name=db_name, table_name=table_name) as gen:
    gen.generate_data(function_list, entries)
