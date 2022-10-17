import json

def create_json():
    skill_dict = {}
    with open("data/relevant_skills.txt","r") as f:
        data = f.readlines()
        data = [i.replace("\n","") for i in data]
        data.remove("")
        for datum in data:
            skill_dict[datum] = ""
    with open("data/skill_mapping.json", "w") as jsonfile:
        json_object = json.dumps(skill_dict, indent=4)
        jsonfile.write(json_object)
~

if __name__ == "__main__":
    print(create_json())