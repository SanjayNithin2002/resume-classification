import csv

def read_skills():
    with open("data/relevant_skills.txt","r") as f:
        data = f.readlines()
        data = [i.replace("\n","") for i in data]
        data.remove("")
    return data

def clean_dataset():
    skills_list = read_skills()
    data = []
    with open("data/dataset.csv","r") as dataset:
        csvreader = csv.reader(dataset)
        for row in csvreader:
            current_row = [skill for skill in row[2:] if skill in skills_list]
            data.append(row[:2] + current_row)
    return data

def create_clean_dataset():
    dataset = clean_dataset()
    with open("data/new_dataset.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(dataset)
            
if __name__ == "__main__" : 
    create_clean_dataset()