from tkinter import filedialog
from unittest import skip
import os

tf = filedialog.askopenfilename(
    initialdir="C:", title="Open Text file", filetypes=(("Text Files", "*.txt"),)
)

file1 = open(tf, "r", encoding="utf8")
Lines = file1.readlines()
cleanup = input("Clean up file? Y/N -")
# cleanupStr = ['flags:','target_id:','object_id:','action_id:','skill_instance_id:','Instant/Triggered actionwas serialized to the client','Client couldn\'t execute','Connecting to instance server','Connect time to instance','Just before calling client','Got Instance Details from login server','Matching object found for','[Hellscape] ExitHellscape','Doodad hash:','Tile hash:']
cleanupStr = ["@from", "@to", "died", "sirus", "maven",'elder', "%", "trade", " : "]
if cleanup.upper() == "Y":
    file3 = open(
        os.environ["USERPROFILE"] + "\Desktop\cleanedUp.txt", "w", encoding="utf8"
    )
    for line in Lines:
        match = 0
        if any(ele in line for ele in cleanupStr):
            file3.writelines(line)
        else:
            skip
    #     for cuStr in cleanupStr:
    #         if cuStr.upper() in line.upper():
    #             match = 1
    #     if match == 0 : file3.writelines(line)
    file3.close()
    exit()

checkStr = input("Search query (separated with , if multiple queries):")
splitStr = checkStr.split(",")

file2 = open(os.environ["USERPROFILE"] + "\Desktop\cropped.txt", "w", encoding="utf8")


# Strips the newline character
for line in Lines:
    for checks in splitStr:
        if checks.upper() in line.upper():
            file2.writelines(line)
        else:
            skip

file2.close()
file1.close()
