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
    translatedText = translator.translate(text, dest=language)
    return translatedText.text


def translateAndroid(filepath, destinationLanguage, fileDirectory):
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
            newText = translate(oldText, destinationLanguage)
            changedText = originalText.replace(oldText, newText)
            f.write('\n' + changedText)
            line = fp.readline()
            cnt += 1

    f.close()


def translateIOS(filePath, destinationLanguage, fileDirectory):
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


originalFile = input("Enter the file path :")
destLanguage = input("Enter destination language code :")
directory = input("Enter the directory path to store the translated file :")
device = input("android or ios ?")

# setup toolbar
# toolbar_width = 40
# sys.stdout.write("[%s]" % (" " * toolbar_width))
# sys.stdout.flush()
# sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['
#
# for i in xrange(toolbar_width):
#     time.sleep(0.1) # do real work here
#     if device.__eq__('android'):
#         translateAndroid(originalFile, destLanguage, directory)
#     elif device.__eq__('ios'):
#         translateIOS(originalFile, destLanguage, directory)
#     # update the bar
#     sys.stdout.write("-")
#     sys.stdout.flush()
#
# sys.stdout.write("\n")
print("Relax a bit ....let me do the translation !!!")
if device.__eq__('android'):
    translateAndroid(originalFile, destLanguage, directory)
elif device.__eq__('ios'):
    translateIOS(originalFile, destLanguage, directory)

print("Hey WakeUp , Ur assigned job is done  !!!")
