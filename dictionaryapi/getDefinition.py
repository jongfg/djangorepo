# author - JonM
# topic - Django Python GeeksforGeeks
# what - use Dictionary api to request definition for word and display on console
# requirements - request user input for word, create request object for api, execute api and display response
# technical specs - use dictionary.com api key (must register), Python3, Import Requests package, JSON payload

# psuedo algorithm
# import requests library
# get input from user as text (word from dictionary)
# create base and query URL for API (include api key and word input)
# execute query against api and receive response data
# convert data from json to object literal
# display data on console

import requests #pip3 install requests
import json

# test console output
print("hello world")

# get input from user
print("Get Definition of word: ")
targetWord = input("Enter a word to lookup: ")
print("You entered the word: " + targetWord)

# build URL
apiKey = "0b0a9ab9-9b89-4c81-90ef-5fb4ba395b29"
print("API key: " + apiKey)
apiURL = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/"
print("API URL: " + apiURL)
targetAPI= apiURL + targetWord + "?key=" + apiKey
print(targetAPI)

# build header
header = {
    'content-type': 'application/json'
}
print("Header: ")
print(header)

# build requests
requestData = requests.get(targetAPI, header)
print("response status: ")
print(requestData)

# display results to console
requestData_json = requestData.json()
print("Defintion object for " + targetWord + ": ")
print(requestData_json)

# test: expected output
""" 
run> python3 getDefinition.py 
console output:
hello world
Get Definition of word: 
Enter a word to lookup: python
You entered the word: python
API key: 0b0a9ab9-9b89-4c81-90ef-5fb4ba395b29
API URL: https://www.dictionaryapi.com/api/v3/references/collegiate/json/
https://www.dictionaryapi.com/api/v3/references/collegiate/json/python?key=0b0a9ab9-9b89-4c81-90ef-5fb4ba395b29
Header: 
{'content-type': 'application/json'}
response status: 
<Response [200]>
Defintion object for python: 
[{'meta': {'id': 'python', 'uuid': 'be1628ad-fd15-492c-84df-76f1f9d41de6', 'sort': '169097000', 'src': 'collegiate', 'section': 'alpha', 'stems': ['python', 'pythons'], 'offensive': False}, 'hwi': {'hw': 'py*thon', 'prs': [{'mw': 'ˈpī-ˌthän', 'sound': {'audio': 'python01', 'ref': 'c', 'stat': '1'}}, {'mw': '-thən'}]}, 'fl': 'noun', 'def': [{'sseq': [[['sense', {'dt': [['text', '{bc}any of various large constricting snakes']], 'sdsense': {'sd': 'especially', 'dt': [['text', '{bc}any of the large oviparous snakes (subfamily Pythoninae of the family Boidae) of Africa, Asia, Australia, and adjacent islands that include some of the largest existing snakes']]}}]]]}], 'art': {'artid': 'python', 'capt': 'python'}, 'et': [['text', 'Latin, monstrous serpent killed by Apollo, from Greek {it}Pythōn{/it}, from {it}Pythō{/it} Delphi']], 'date': 'circa 1825', 'shortdef': ['any of various large constricting snakes; especially : any of the large oviparous snakes (subfamily Pythoninae of the family Boidae) of Africa, Asia, Australia, and adjacent islands that include some of the largest existing snakes']}] 

end output"""