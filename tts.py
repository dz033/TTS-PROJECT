#this part is for processing a document into words, and then converting into phonetics
#phonetics might be tricky 
import winsound
import requests
import asyncio

phoneticDict = {}
phoneticListC = ["b", "d", "f", "g", "h", "dʒ", "k", "l", "m", "n", "p", "r", "s", "t", "v", "w", "z" , "ʒ"
                , "tʃ", "ʃ", "θ", "ð", "ŋ", "j"]
phoneticListV = ["æ", "eɪ", "ɛ", "i:", "ɪ", "aɪ", "ɒ", "oʊ", "ʊ", "ʌ", "u:", "ɔɪ", "aʊ", "ə", "eəʳ", "ɑ:"
                 , "ɜ:ʳ", "ɔ:", "ɪəʳ", "ʊəʳ"]
phoneticListAll = phoneticListC + phoneticListV #not sure if they would be more useful together or separated

def getPhonetics(word):
    #grab the phonetics string from dictionary api
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    info = response.json()
    phonetics = info[0]["phonetic"]
    return phonetics.strip("/")

def getFox(): #for me to understand how to use api requests :)
    response = requests.get("https://randomfox.ca/floof/")
    print(response.text)

def pronounceWord(phonetics):
    for char in phonetics:
        if char in phoneticListAll:
            pronounce(char)
        elif char == "ˈ":
            pass



def pronounce(phoneme):
    winsound.PlaySound(f"{phoneme}.wav", winsound.SND_FILENAME)
    return None

def main():

    sampleText = input("Type or paste a paragraph. (only text at the moment please!)")
    l1 = sampleText.split(" ")
    for word in l1:
        pronounceWord(word)
        #add some kind of delay between words.

#pronounce("poopootesting")
#getFox()
#getPhonetics("bet")
pronounceWord("fd") # pacing is not consistent... hm