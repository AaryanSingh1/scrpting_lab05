import re
from collections import Counter
import csv

#open and close log file
def reader(filename):
    with open(filename) as f:
        log = f.read()
        print(log)

        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ips_list = re.findall(regexp, log)
        return(ips_list)    

#this function will count the number of times the ip address is repeated
def count(ips_list):
    return Counter(ips_list)

#this will write the output in a csv file
def write_csv(Counter):
    with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)

        header = ['IP', 'Frequency']
        writer.writerow(header)

        for item in Counter:
            writer.writerow((item, Counter[item]))

#creating the second output csv file
output2nd = open('output2.csv', 'w')

#assigning headers
writer = csv.writer(output2nd)
writer.writerow(['Date', 'Time', 'Username', 'IP Address'])

#specifying path
log_file = open('C:\scrpting_lab05\log')

#this will get the required data 
for x in log_file.readlines():
    log = x.split(":")[len(x.split(":"))-1].lower()

    find = re.search(r'SRC=\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', log)

    if (find != None):

        if log[find.span()[0]+4:find.span()[1]] in {}:
            lib = {}[log[find.span()[0]+4:find.span()[1]]] = lib + 1
        
        else:
            lib = 1

    find2nd = re.search(r'invalid', log)
    if (find2nd != None):
        
        #this will put the data in the csv file in the correct order
        structure = [" ".join(x.split(" ")[0:2]), x.split(" ")[2], log.split(" ")[3],
                        log.split(" ")[len(log.split(" "))-1]]

        CSV = ",".join(structure) 
        
        output2nd.write(CSV)


if __name__ == '__main__':
    write_csv(count(reader('log')))