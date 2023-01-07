import os
import os.path
from storing.saved import data

save_path = 'storing'
file_name = "saved.py"

completeName = os.path.join(save_path, file_name)

def save(bank):
    dataList = bank.saveAll()
    timesPlayed = int(data[2]) + 1
    with open(completeName, 'w') as file:
        outputStr = ""
        outputStr += "data = "
        dataList.append(timesPlayed)
        outputStr += str(dataList)
        file.write(outputStr)