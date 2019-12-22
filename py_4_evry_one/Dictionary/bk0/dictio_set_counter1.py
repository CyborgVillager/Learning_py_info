word = 'Jonathan Almawi'
word02 = 'brontosaurus'

#get info for word
def word0():
    dictio = dict()
    for dicto_info in word:
        if dicto_info not in dictio:
            dictio[dicto_info] = 1
        else:
            dictio[dicto_info] = dictio[dicto_info] + 1
    print(dictio)

#get info for word2
def word2():
    dictio2 = dict()
    for dicto_info2 in word02:
        if dicto_info2 not in dictio2:
            dictio2[dicto_info2] = 1
        else:
            dictio2[dicto_info2] = dictio2[dicto_info2] + 1
    print(dictio2)

def main():
    word0()
    word2()

main()


# basic histogram / counter
# 'The for loop ' travels the string. Each time through the loop if the dicto_info is not in the dicto,
# the system iwll create a new item with the key dictio_info and the inital val by 1. If the info is already in
# just increment dictio[dicti_info]