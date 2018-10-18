import os
import time
import sys

from googletrans import Translator


def translate(text, language):
    translator = Translator()
    Translator(service_urls=[
        'translate.google.com',
        'translate.google.co.in',
    ])
    print(" This is the text to be printed")
    print(text)
    translated_text = translator.translate(text, dest=language)
    return translated_text.text


def translateAndroid(filepath, destinationLanguage, fileDirectory):
    print("Relax a bit ....translateAndroid !!!")

    fileDirectory = fileDirectory + '/values-' + destinationLanguage
    if not os.path.exists(fileDirectory):
        os.makedirs(fileDirectory)

    androidFilePath = fileDirectory + '/strings.xml'
    f = open(androidFilePath, 'w')
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            originalText = line.strip()
            startInt = originalText.find('">') + 2
            endInt = originalText.find('</')
            oldText = originalText[startInt:endInt]
            print("Old Text ")
            print(oldText)
            print("newText")
            print(translate(oldText, destinationLanguage))
            newText = translate(oldText, destinationLanguage)

            changedText = originalText.replace(oldText, newText)
            f.write('\n' + changedText)
            line = fp.readline()
            cnt += 1

    f.close()


def translateIOS(filePath, destinationLanguage, fileDirectory):
    print("Relax a bit ....translateIOS !!!")
    if not os.path.exists(fileDirectory):
        os.makedirs(fileDirectory)

    iosFilePath = fileDirectory + '/Localizable.strings'
    f = open(iosFilePath, 'w')
    with open(filePath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            originalText = line.strip()
            startInt = originalText.find('=')
            endInt = originalText.find('";')
            oldText = originalText[startInt:endInt]
            newText = translate(oldText, destinationLanguage)
            changedText = originalText.replace(oldText, newText)
            f.write('\n' + changedText)
            line = fp.readline()
            cnt += 1
    f.close()


# originalFile = input("Enter the file path :")
originalFile = "/Users/nitish/Workspace/Tarento/Android/M2M/app/src/main/res/values/strings.xml"
# destLanguage = input("Enter destination language code :")
destLanguage = "sv"
# directory = input("Enter the directory path to store the translated file :")
directory = "/Users/nitish/Workspace/Tarento/Android/"
# device = input("android or ios ?")
device = "android"


print("Relax a bit ....let me do the translation !!!")
if device.__eq__('android'):
    translateAndroid(originalFile, destLanguage, directory)
elif device.__eq__('ios'):
    translateIOS(originalFile, destLanguage, directory)

print("Hey WakeUp , Ur assigned job is done  !!!")
