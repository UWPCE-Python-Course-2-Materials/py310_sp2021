# pip install pysnooper

import pysnooper

@pysnooper.snoop()
def censor(text, word):
    while word in text:
        text = (
            text[: text.find(word)]
            + "*" * len(word)
            + text[text.find(word) + len(word) :]
        )
    return text


print(censor("blah andy blah blah", "andy"))
