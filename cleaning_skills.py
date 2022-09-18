import json
import csv

def clean_skills():
    with open("data/skill_mapping.json","r") as skills_json:
        json_data = json.load(skills_json)


    with open("data/new_dataset.csv","r") as f:
        dataset = []
        csvfile = csv.reader(f)
        for data in csvfile:
            row = sorted(set([json_data[skill] for skill in data[2:]]))
            dataset.append(data[:2] + row)
    return dataset

def write_csvfile():
    dataset = clean_skills()
    with open("data/clean_dataset.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(dataset)            

            

if __name__ == "__main__" :
    write_csvfile()