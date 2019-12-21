from question import Question
question_prompts = [
    'What color are apples?\n(a) red/green\n(b) Purple\n(c) Orange\n\n',
    'what color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n',
    'What color are stawberries?\n(a) Yellow\n(b) red\n(c) Blue\n\n'
]

questions = [
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'c'),
    Question(question_prompts[2], 'b'),
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print('Your score is ' + str(score) + ' out of ' + str(len(questions) )+ ' correct')

run_quiz(questions)