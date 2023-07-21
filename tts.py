#this part is for processing a document into words, and then converting into phonetics
#phonetics might be tricky 
import winsound
import requests

phoneticDict = {}

def getPhonetics(word):
    #grab the phonetics string from dictionary api
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    info = response.json()
    phonetics = info[0]["phonetic"]
    print(phonetics)


def getFox(): #for me to understand how to use api requests :)
    response = requests.get("https://randomfox.ca/floof/")
    print(response.text)

def pronounce(phoneme):
    winsound.PlaySound("poopootesting.wav", winsound.SND_FILENAME)
    return None

def main():

    sampleText = input("Type or paste a paragraph. (only text at the moment please!)")
    l1 = sampleText.split(" ")
    #for word in l1:
    #    pronounce(phoneticDict[word])

#pronounce("a")
#getFox()
getPhonetics("bet")