from tkinter import filedialog
from unittest import skip


data = [("Text Files(*.txt)", "*.txt")]
tf = filedialog.askopenfilename(
    initialdir="C:", title="Open Text file", filetypes=(("Text Files", "*.txt"),)
)

mainFile = open(tf, "r", encoding="utf8")
Lines = mainFile.readlines()
cleanup = input("Clean up file? Y/N -")
# cleanupStr = ['flags:','target_id:','object_id:','action_id:','skill_instance_id:','Instant/Triggered actionwas serialized to the client','Client couldn\'t execute','Connecting to instance server','Connect time to instance','Just before calling client','Got Instance Details from login server','Matching object found for','[Hellscape] ExitHellscape','Doodad hash:','Tile hash:']
cleanupStr = ["@from", "@to", "died", "sirus", "maven", "elder", "%", "trade", " : "]
if cleanup.upper() == "Y":
    fileSaveClean = filedialog.asksaveasfilename(
        defaultextension=data,
        filetypes=data,
        initialdir="C:",
        title="Choose a save location of file",
    )
    with open(fileSaveClean, "w", encoding="utf8") as fileClean:
        for line in Lines:
            match = 0
            if any(ele in line for ele in cleanupStr):
                fileClean.writelines(line)
            else:
                skip
        fileClean.close()
        exit()

checkStr = input("Search query (separated with , if multiple queries):")
splitStr = checkStr.split(",")

fileSaveCrop = filedialog.asksaveasfilename(
    defaultextension=data,
    filetypes=data,
    initialdir="C:",
    title="Choose a save location of file",
)
with open(fileSaveCrop, "w", encoding="utf8") as fileCrop:

    for line in Lines:
        if any(ele in line for ele in splitStr):
            fileSaveCrop.writelines(line)
        else:
            skip

fileCrop.close()
mainFile.close()
