import csv
import ast
import os

if __name__ == '__main__':
    data = 'data_input/Occupations.csv'
    file = open(data, "r")
    csv_reader = csv.reader(file)

    lists_from_csv = []
    lists_to_csv = []
    for row in csv_reader:
        lists_from_csv.append(row)
    for n in lists_from_csv:
        topic_id = n[0]

        for occup in n[1:]:
            if occup != '':
                of = ast.literal_eval(occup)
                for key in of:
                    for i in of[key]:
                        occupation_tuple = (topic_id, i)
                        lists_to_csv.append(occupation_tuple)

    if not os.path.exists('output'):
        os.makedirs('output')
    with open('output/occupations.csv', 'w') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(['talk_id', 'occupations'])
        for row in lists_to_csv:
            csv_out.writerow(row)
