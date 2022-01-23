import csv
import ast
import os

if __name__ == '__main__':
    data = 'data_input/Related Topics.csv'
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
                related_topic = ast.literal_eval(topic)
                for key in related_topic:
                    topic_tuple = (topic_id, key)
                    lists_to_csv.append(topic_tuple)
    print(lists_to_csv)

    if not os.path.exists('output'):
        os.makedirs('output')
    with open('output/related_topics.csv', 'w') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(['talk_id', 'related_talks'])
        for row in lists_to_csv:
            csv_out.writerow(row)
