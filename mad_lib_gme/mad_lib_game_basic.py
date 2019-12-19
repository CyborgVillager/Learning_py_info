def mad_lib_no_user_input_1st():
    print('A.I is {plural_noun} ')
    print('The Sky is  {color} ')
    print('You have to write a color & a noun to explain the story')


def mad_lib_story_explained():
    plural_noun = input("Enter a Plural Noun: ")
    color = input("Enter a color: ")

    print('A.I is ' + plural_noun + '!')
    print('The Sky is ' + color)


def space():
    print('--------Respond Accordinaly--------')

def main():
    mad_lib_no_user_input_1st()
    space()
    mad_lib_story_explained()

main()
