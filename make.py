import csv
import copy
import json
import random


def printFunction(reader , _max):
    header = next(reader)
    count = 0
    temp = []
    list = []

    for row in reader:
        dialogLine = row["conversation_id"]
        
        if int(dialogLine) == 1:
            if temp != [] :
                copied_list = copy.deepcopy(temp)
                list.append(copied_list)
            temp.clear()
            temp2 = {
                "q": row["kor_sent"],
                "a": row['eng_sent']
            }
            temp.append(temp2)
            count += 1
            if count == _max + 1 :
                return list
        else:
            temp2 = {
                "q": row["kor_sent"],
                "a": row['eng_sent']
            }
            temp.append(temp2)

def main():
    myList = []
    with open('conversations.csv', 'r', encoding='utf-8-sig') as data_file:
        reader = csv.DictReader(data_file, ["date", "conversation_id", "kor_sent", "eng_sent"])
        myList = printFunction(reader , 20)
    fileCount = 1
    for con in myList :
        filePath = f"JSON/level-{fileCount}.json"
        levelData = []
        for ques in con :
            random_number = random.randint(-1, 4)
            ans = ["","",""]
            ans.insert(random_number, ques["a"])
            obj = {
                "question": ques["q"],
                "answers": ans,
                "correct": ques["a"]
            }
            levelData.append(obj)

        base = {
            "id":"con-game",
            "level":fileCount,
            "data": levelData
        }
        with open(filePath, 'w',encoding='utf-8') as file:
            json.dump(base, file , ensure_ascii=False)
            print(f"{filePath} - file Saved ")
        fileCount += 1

main()