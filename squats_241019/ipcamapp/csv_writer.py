import csv


def csv_writer_func(data):
    with open("dimensions.csv", "a") as csv_file:
        writer = csv.writer(csv_file)
        for line in data:
            writer.writerow(line)