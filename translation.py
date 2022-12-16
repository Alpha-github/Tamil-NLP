import requests
import os
from tamil import utf8
string = u"எஃகு"
letters = utf8.get_letters(string)
print(letters)
for letter in letters:
    print(letter)


url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": os.getenv("X-RapidAPI-Key"),
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

def english_tamil(text):
    long_list_of_words = text.split(' ')
    url_encoded_text = f"q={'%20'.join(long_list_of_words)}"
    payload = url_encoded_text+"&target=ta&source=en"

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text.encode('utf-8'))

# english_tamil("Hello")
