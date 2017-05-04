# PyCleaner
This program is a simple Desktop cleaner that will only move files, not folders, into a folder called Desktop located on your Desktop including subfolders for Python scripts, Jpeg Pictures, and Word Documents.

## Methods
In order to make this program more universal and modifiable, I created methods in order to generalize the script to whichever extension/file type I prefer. Here is the main method:
```
def moveFilesOfType(fromDir, toDir, extension):
    ls = os.listdir(fromDir)
    for filename in ls:
        if filename.endswith(extension):
            os.rename(fromDir + filename, toDir + filename)
```
This method was specifically in order to sort the files into the correct subfolder if it exists. In order to make another folder, you'll have to alter the ```folders()``` function.
