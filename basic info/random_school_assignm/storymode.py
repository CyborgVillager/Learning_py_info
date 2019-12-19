while True:
    check_info = input('To see your profile type: A)' + 'or to see your posts type: B) ')

#check if A or B has been selected
    if check_info in ['A','B']:

        break

#functions w/specific side quest

def check_profile():
    user_name = input('What is your username? ')
    age = input('How old are you? ')
    gender = input('What is your gender? ')
    complete_sentence = ('Your username is' + user_name + ' and you are' + age + 'years old' +
          'your gender is', gender)
    print(complete_sentence)

def check_posts():
    post_name = input('What is your post name? ')
    post_age = input('What date did you post your upload? ')
    gender = input('What is your gender? ')
    complete_sentence_01 = ('Your post name is ' + post_name + ' and your upload age is' + post_age + 'days old' +
                           'and your gender is' + gender)
    print(complete_sentence_01)

if check_info == 'A':
    check_profile()
elif check_info == 'B':
    check_posts()


