def caps(word):
    if len(word)==1:
        if word.isupper():
            return word.lower()
        else:
            return word.upper()
    if word.isupper():
        return word.lower()
    if word[1:].isupper() and word[0].islower():
        return word.capitalize()
    return word
word=input().strip()
print(caps(word))