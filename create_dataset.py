import os
import json
import csv
import re

def get_files(path):
    files = os.listdir(path)
    return files

def open_file(file_path):
    f = open(file_path,encoding="utf8")
    data = json.load(f)
    current_list = []
    for i in range(25): 
        name = data['resumes'][i]['data']["name"]["raw"]
        skills = [i["name"] for i in data['resumes'][i]['data']["skills"]]
        skills = [ re.sub(r" ?\([^)]+\)", "",skill) for skill in skills]
        current_data = [name] + skills
        current_list.append(current_data)
    return current_list

def dataset_creation():
    files_list = get_files("json2")
    total_data = []
    for i in files_list:
        total_data += open_file("json2/{path}".format(path = i))
    total_data = [[i+1] + total_data[i] for i in range(len(total_data))]
    filename = "data/dataset2.csv"
    with open(filename, 'w') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerows(total_data)



if __name__ == "__main__" :
    dataset_creation()
    

