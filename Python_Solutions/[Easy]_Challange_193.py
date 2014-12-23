def acronyms(word):
    abbreviations = {
        "lol": "laugh out loud",
        "dw": "don't worry",
        "dwi": "deal with it",
        "hf": "have fun",
        "gg": "good game",
        "brb": "be right back",
        "g2g": "got to go",
        "gtg": "got to go",
        "wtf": "what the frig",
        "wp": "well played",
        "gl": "good luck",
        "imo": "in my opinion",
        "omw": "on my way",
        "ttyl": "talk to you later",
    }

    for x in abbreviations:
        if x == word:
            return abbreviations[word]
    return word

def main(text):
    words = text.split(" ")
    for word in words:
        print acronyms(word),
main(raw_input())
