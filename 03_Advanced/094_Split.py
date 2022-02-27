import time

def separateur(text, sep):
    return_list = []
    while True:
        pos = text.find(sep)
        if pos == -1:
            return_list.append(text)
            break
        return_list.append(text[0:pos])
        text = text[pos+1:]
    return return_list

phrase = "bonjour-tout-le-monde"
print(separateur(phrase, "-"))