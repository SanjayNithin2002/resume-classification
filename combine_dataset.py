import csv

def extract_results():
    with open("temp.csv","r") as f:
        data = [row[2].lower() for row in csv.reader(f)]
        
    return data


def combine_dataset():
    with open('data/dataset.csv', 'r') as f1, open('data/dataset2.csv', 'r') as f2, open('final_datasets/complete_dataset.csv', 'w') as f3:
        f1_reader = csv.reader(f1)
        f2_reader = csv.reader(f2)
        f3_writer = csv.writer(f3)
        data = extract_results()
        pointer = 0
        for row in f1_reader:
            f3_writer.writerow(row[:2] + [data[pointer]] + row[2:])
            pointer += 1
        x = 201
        for row in f2_reader:
            f3_writer.writerow([x] + row[1:2] + [data[pointer]] + row[2:])
            x+=1
            pointer += 1


if __name__ == "__main__" :
    combine_dataset()