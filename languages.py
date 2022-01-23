import csv
import ast
import os

if __name__ == '__main__':
    data = 'data_input/Languages.csv'
    file = open(data, "r")
    csv_reader = csv.reader(file)

    lists_from_csv = []
    lists_to_csv = []
    for row in csv_reader:
        lists_from_csv.append(row)
    for n in lists_from_csv:
        talk_id = n[0]

        for lang in n[1:]:
            if lang != '':
                print(lang)
                lang_list = (ast.literal_eval(lang))
                lang_tuple = (talk_id, len(lang_list))
                lists_to_csv.append(lang_tuple)

    if not os.path.exists('output'):
        os.makedirs('output')
    with open('output/languages.csv', 'w') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(['talk_id', 'available_lang'])
        for row in lists_to_csv:
            csv_out.writerow(row)
