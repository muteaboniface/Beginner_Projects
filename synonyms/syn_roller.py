from bs4 import BeautifulSoup
import sys
import json
import re
import requests

def Syn_Roller():
    """
    This method has drawn insights from Thom Irves Work featured in his 
    blog IntegratedMachineLearningand Ai.
    """

    word = input('Welcome to synonym roll:\n Enter word to query :  ')

    URL = f'https://www.thesaurus.com/browse/{word}'

    page = requests.get(URL)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
    else:
        print("No Synonyms for that word")
        return "No Synonyms for that word"

    the_script = soup.find(text=re.compile("window.INITIAL_STATE"))

    the_script = the_script.replace("window.INITIAL_STATE = ", "")
    the_script = the_script.replace(':undefined', ':"undefined"')
    the_script = the_script.replace(';', '')

    data = json.loads(the_script)

    with open('test1.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    synonyms = {}
    synonyms[word] = {}
    for each_tab in data["searchData"]["tunaApiData"]["posTabs"]:
        for syn in each_tab["synonyms"]:
            sim = float(syn["similarity"])
            if sim not in synonyms[word].keys():
                synonyms[word][sim] = []
            synonyms[word][sim].append(syn["term"])

    k = synonyms[word].keys()
    print("Synonyms interms of strength values are: \n")
    for strength in k:
        print(f'\n{strength} Synonym Strength')
        print(synonyms[word][strength])
        
Syn_Roller()
