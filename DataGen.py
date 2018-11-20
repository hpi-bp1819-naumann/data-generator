import psycopg2

class DataGenerator:
    # generates random data according to given functions and saves them to database

    def __init__(self, host, user, password, db_name, table_name):
        self.connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                dbname=db_name
        )
        self.cursor = self.connection.cursor()
        self.table_name = table_name

    def __enter__(self):
        return self

    def __exit__(self):
        self.connection.close()

    # generates datarecord
    def generate_record(self, function_list, counter):
        record = {}
        for function in function_list:
            record[function] = function_list[function]["function"](counter)
        
        return record

    def create_table(self, function_list):
        column_strings = []
        for i in function_list:
            column_strings.append(i + " " + function_list[i]["sql_type"])
        query_string = """CREATE TABLE IF NOT EXISTS {0} ({1});""".format(self.table_name, ','.join(column_strings))
        self.cursor.execute(query_string)
        self.connection.commit()

    def add_record_to_database(self, record):
        query_string = """INSERT INTO {0} ({1}) VALUES({2});""".format(self.table_name, ','.join(record), ','.join(record.values()))
        self.cursor.execute(query_string)

    def generate_data(self, function_list, count):
        self.create_table(function_list)
        for i in range(count):
            record = self.generate_record(function_list, i)
            self.add_record_to_database(record)
        self.connection.commit()
