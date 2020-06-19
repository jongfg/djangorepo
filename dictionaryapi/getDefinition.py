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