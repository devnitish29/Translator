import os

from googletrans import Translator

translator = Translator()
originalFile = input("Enter the file path :")
language = input("Enter destination language code :")
fileDirectory = input("Enter the directory path to store the translated file :")
print("Relax a bit ....let me do the translation !!!")
directory = fileDirectory + '/values-' + language;
if not os.path.exists(directory):
    os.makedirs(directory)
newFilePath = directory + '/strings.xml'
f = open(newFilePath, 'w')
with open(originalFile) as fp:
    with open(originalFile) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            originalText = line.strip()
            startInt = originalText.find('">') + 2
            endInt = originalText.find('</')
            oldText = originalText[startInt:endInt]
            translatedText = translator.translate(oldText, dest=language)
            newText = translatedText.text
            changedText = originalText.replace(oldText, newText)
            f.write('\n' + changedText)
            line = fp.readline()
            cnt += 1

f.close()
print("Hey WakeUp , Ur assigned job is done  !!!")
