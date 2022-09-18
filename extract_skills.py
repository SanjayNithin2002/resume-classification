import numpy as np
import csv

def extract_skills():
    skills_arr = np.array([],dtype='object')
    with open('data/dataset.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            skills_arr = np.append(skills_arr,line[2:])
    return np.unique(skills_arr)

def write_skills():
    skills_arr = extract_skills()
    with open("data/skills.txt","w") as file:
        for skill in skills_arr:
            file.write(skill + "\n")

if __name__ == "__main__":
    write_skills()