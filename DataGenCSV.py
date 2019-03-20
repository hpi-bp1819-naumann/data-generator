import csv
import random


class DataGenerator:
    # generates random data according to given functions and saves them to database

    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return self

    # generates datarecord
    def generate_record(self, function_list, counter):
        record = {}
        for f in function_list:
            record[f] = function_list[f]["function"](counter, record)

        return record

    def print_progress_bar(self, iteration, total, length):
        percent = ("{0:.2f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = '█' * filledLength + '-' * (length - filledLength)
        print('\rProgress: |%s| %s%% Complete' % (bar, percent), end='\r')
        # Print New Line on Complete
        if iteration == total:
            print()

    def generate_data(self, function_list, count):
        with open(self.file_name, 'w') as csvfile:
            fieldnames = function_list.keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for i in range(count):
                record = self.generate_record(function_list, i)

                writer.writerow(record)
                self.print_progress_bar(i + 1, count, 50)
