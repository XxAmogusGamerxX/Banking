import os


def save(dataList: list,timesPlayed):
    with open('storing\saved.py', 'w') as file:
        outputStr = ""
        outputStr += "data = "
        dataList.append(timesPlayed)
        outputStr += str(dataList)
        file.write(outputStr)