import csv

def read_data():

    with open('data.csv', 'r', encoding='UTF-8') as f:
        reader = csv.reader(f, delimiter=',')
        user_list = []
        for row in reader:
            user_list.append(row)
            return user_list
