import requests
import os
from urllib.parse import quote
import json
import openai

def english_tamil_google(text):
    '''English to Tamil translation using Google Translate
    To subscribe: https://rapidapi.com/googlecloud/api/google-translate1/pricing'''

    url_encoded_text = f"q={quote(text)}"
    payload = url_encoded_text+"&target=ta&source=en"
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": os.getenv("X-RapidAPI-Key"),
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return(json.loads(response.text)['data']['translations'][0]['translatedText'])

def tamil_english_google(text):
    '''Tamil to English translation using Google Translate
    To subscribe: https://rapidapi.com/googlecloud/api/google-translate1/pricing'''

    url_encoded_text = f"q={quote(text)}"
    payload = url_encoded_text+"&target=en&source=ta"
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": os.getenv("X-RapidAPI-Key"),
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return(json.loads(response.text)['data']['translations'][0]['translatedText'])

def english_tamil_rapid(text):
    '''English to Tamil translation using Rapid Translate Multi Traduction
    To subscribe: https://rapidapi.com/sibaridev/api/rapid-translate-multi-traduction/pricing'''

    url = "https://rapid-translate-multi-traduction.p.rapidapi.com/t"
    payload = {
        "from": "en",
        "to": "ta",
        "e": "",
        "q": [text]
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": os.getenv("X-RapidAPI-Key"),
        "X-RapidAPI-Host": "rapid-translate-multi-traduction.p.rapidapi.com"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    return(json.loads(response.text)[0])

def tamil_english_rapid(text):
    '''Tamil to English translation using Rapid Translate Multi Traduction
    To subscribe: https://rapidapi.com/sibaridev/api/rapid-translate-multi-traduction/pricing'''

    url = "https://rapid-translate-multi-traduction.p.rapidapi.com/t"
    payload = {
        "from": "ta",
        "to": "en",
        "e": "",
        "q": [text]
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": 'ec710db6e0msh09051ac0e88c23ap18a531jsn9a7186571b67',
        "X-RapidAPI-Host": "rapid-translate-multi-traduction.p.rapidapi.com"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    return(json.loads(response.text)[0])

def english_tamil_translo(text):
    '''English to Tamil translation using Translo API
    To subscribe: https://rapidapi.com/armangokka/api/translo/pricing'''

    url = "https://translo.p.rapidapi.com/api/v3/translate"
    s = quote(text)
    payload = "from=en&to=ta&text="+s
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": os.getenv("X-RapidAPI-Key"),
        "X-RapidAPI-Host": "translo.p.rapidapi.com"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return json.loads(response.text)['translated_text']

def tamil_english_translo(text):
    '''Tamil to English translation using Translo API
    To subscribe: https://rapidapi.com/armangokka/api/translo/pricing'''

    url = "https://translo.p.rapidapi.com/api/v3/translate"
    s = quote(text)
    payload = "from=ta&to=en&text="+s
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": os.getenv("X-RapidAPI-Key"),
        "X-RapidAPI-Host": "translo.p.rapidapi.com"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return json.loads(response.text)['translated_text']


#*********************************************************************************************************************
#*********************************************************************************************************************


openai.api_key = os.getenv("OPENAI_API_KEY")

def text_davinci(text,max_tokens=2048):
    '''Provides Response to given question using text-davinci-003 GPT3 engine'''

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=0,
        max_tokens=max_tokens,
    )
    return response['choices'][0]['text'][2:]

def sensitivity(text, temperature=0, max_tokens=1, top_p=0, logprobs=10):
    """This gives the sensitivity rating of the text
    0 - The text is safe.
    1 - This text is sensitive.
        This means that the text could be talking about a sensitive topic,
        something political, religious, or talking about a protected class such as race or nationality.
    2 - This text is unsafe.
    This means that the text contains profane language, prejudiced or hateful language,
    something that could be NSFW, or text that portrays certain groups/people in a harmful manner.

    More info: https://beta.openai.com/docs/models/content-filter"""

    response = openai.Completion.create(
        model="content-filter-alpha",
        prompt="<|endoftext|>" + text + "\n--\nLabel:",
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        logprobs=logprobs,
    )
    output = response["choices"][0]["text"]
    toxic_threshold = -0.355

    if output == "2":
        logprobs = response["choices"][0]["logprobs"]["top_logprobs"][0]
        if logprobs["2"] < toxic_threshold:
            logprob_0 = logprobs.get("0", None)
            logprob_1 = logprobs.get("1", None)
            if logprob_0 is not None and logprob_1 is not None:
                if logprob_0 >= logprob_1:
                    output = "0"
                else:
                    output = "1"
            elif logprob_0 is not None:
                output = "0"
            elif logprob_1 is not None:
                output = "1"

    if output not in ["0", "1", "2"]:
        output = "2"

    return output
