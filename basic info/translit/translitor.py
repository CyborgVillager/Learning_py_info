# cyborgian lang
# vowls -> ci
#dog -> dcig
#cat -> ccit

def translate(phrase):
    translation = ' '
    for letter in phrase:
        if letter.lower() in 'aeiou':
            if letter.isupper():
                translation = translation + 'Ci'
            else:
                translation = translation + 'ci'
        else:
            translation = translation + letter
    return translation

print(translate(input('Enter a phrase: ')))