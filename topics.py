import csv
import os

if __name__ == '__main__':
    data = 'data_input/topics.csv'
    file = open(data, "r")
    csv_reader = csv.reader(file)

    lists_from_csv = []
    lists_to_csv = []
    for row in csv_reader:
        lists_from_csv.append(row)
    for n in lists_from_csv:
        topic_id = n[0]

        for topic in n[1:]:
            if topic != '':
                t = (topic_id, topic)
                lists_to_csv.append(t)
    print(lists_to_csv)

    if not os.path.exists('output'):
        os.makedirs('output')
    with open('output/topics.csv', 'w') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(['id', 'topic'])
        for row in lists_to_csv:
            csv_out.writerow(row)

