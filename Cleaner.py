import os
import shutil

srcDir = os.listdir('//Users/julianboaz/Desktop')

def folders():
    os.chdir('//Users/julianboaz/Desktop')
    os.makedirs('Desktop/Documents')
    os.chdir('//Users//julianboaz//Desktop//Desktop')
    os.makedirs('Scripts')
    os.chdir('//Users//julianboaz//Desktop//Desktop')
    os.makedirs('Pictures')



if not os.path.isdir('//Users/julianboaz/Desktop/Desktop'):
    folders()

def deleteMeta(period):
    for x in srcDir:
        if x.startswith(period) in srcDir:
            srcDir.pop(x)

deleteMeta('.')




def moveFilesOfType(fromDir, toDir, extension):
    ls = os.listdir(fromDir)
    for filename in ls:
        if filename.endswith(extension):
            os.rename(fromDir + filename, toDir + filename)

moveFilesOfType('//Users/julianboaz/Desktop/', '//Users/julianboaz/Desktop/Desktop/Documents/', '.docx')
moveFilesOfType('//Users/julianboaz/Desktop/', '//Users/julianboaz/Desktop/Desktop/Scripts/', '.py')
moveFilesOfType('//Users/julianboaz/Desktop/', '//Users/julianboaz/Desktop/Desktop/Pictures/', '.jpg')

for x in srcDir:
    file = os.path.join('//Users/julianboaz/Desktop', x)
    if (os.path.isfile(file)):
        shutil.move(file, '//Users/julianboaz/Desktop/Desktop')
