import os

from googletrans import Translator

translator = Translator()
language ="sv"
filepath = '/home/nitish/Desktop/testStrings.text';
directory = '/home/nitish/Desktop/values-'+language;
if not os.path.exists(directory):
    os.makedirs(directory)
newFilePath =directory+'/strings.xml'
f =open(newFilePath,'w')
with open(filepath) as fp:
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            originalText = line.strip()
            startInt = originalText.find('">') + 2
            endInt = originalText.find('</')
            oldText = originalText[startInt:endInt]
            translatedText = translator.translate(oldText,dest=language)
            newText= translatedText.text
            print(oldText)
            print(newText)
            changedText=  originalText.replace(oldText,newText)
            print(changedText)
            f.write('\n'+changedText)
            line = fp.readline()
            cnt += 1

f.close()