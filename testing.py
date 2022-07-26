import re
import csv

def invalid_user(filename):
    with open(filename, 'r') as f:
        log = f.readlines()
        print(log)

        regexp = r"^(.{6}) (.*) myth .* user (.*) from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
        
        for x in log:
            get = re.search(regexp, x)
            print(get)

def write_csv2(Counter):
    with open('output2.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)

        header = ['Date', 'Time', 'Username', 'IP Address']
        writer.writerow(header)

        

write_csv2(invalid_user('log'))