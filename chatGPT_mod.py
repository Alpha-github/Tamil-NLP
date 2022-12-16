import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def text_davinci(text,max_tokens=2048):
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

print(text_davinci("thirukural"))
