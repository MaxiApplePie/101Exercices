def join(separator, *words):
    joined_words = ''
    for w in words:
        joined_words += w + separator
    return joined_words[0:-1]


j = join(":", "Bonjour", "tout", "le", "monde")
print(j)