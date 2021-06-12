import csv


def read_csv(filename):
    with open(filename) as file:
        file_data = csv.reader(file)
        headers = next(file_data)
        return [dict(zip(headers, i)) for i in file_data]


def search(list_data, **kw):
    return filter(lambda i: all((i[k] == v for (k, v) in kw.items())), list_data)


def write_csv(filename, data, columns):
    with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(data)


# begin logic
data = read_csv('electronic-card-transactions-may-2021-csv-tables.csv')

only_percent = list(search(data, UNITS='Percent'))

for row in only_percent:
    row['Suppressed'] = 'Yes'

write_csv('modified.csv', data, data[0].keys())
