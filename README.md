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

## Specific to mac
In this script, I had to add a method specific to mac because there's hidden Meta Data on the Desktop that is recreated upon deletion. In order to ignore the Meta Data I had to write the following method:
```
def deleteMeta(period):
    for x in srcDir:
        if x.startswith(period) in srcDir:
            srcDir.pop(x)
```
Following this I call the method with the parameter of period like so: ```deleteMeta('.')``` This takes everything that starts with a period (hidden files) and ignores them from that array.

## Moving Files
I needed to find a way to move everything and so I wrote this:
```
for x in srcDir:
    file = os.path.join('//Users/julianboaz/Desktop', x)
    if (os.path.isfile(file)):
        shutil.move(file, '//Users/julianboaz/Desktop/Desktop')
```
This just takes everything off the Desktop and moves it rather than copying it.

## Ugly Functions
Unfortunately I don't see a way to clean this up as it's pretty bare bones as it is. If you can help me clean up the following:
```
def folders():
    os.chdir('//Users/julianboaz/Desktop')
    os.makedirs('Desktop/Documents')
    os.chdir('//Users//julianboaz//Desktop//Desktop')
    os.makedirs('Scripts')
    os.chdir('//Users//julianboaz//Desktop//Desktop')
    os.makedirs('Pictures')
```
It would be greatly appreciated.

Julian Boaz
