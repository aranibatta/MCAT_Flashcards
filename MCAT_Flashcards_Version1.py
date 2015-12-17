import os, random

count = 0
score = 0

file1 = open('MCAT_Flashcards_Questions.txt', 'r')
file2 = open('MCAT_Flashcards_Answers.txt', 'r')

f1content = file1.readlines()
f2content = file2.readlines()

while count < 5:
    os.system('clear')

    wordnum = random.randint(0, len(f1content)-1)

    print('Question:', f1content[wordnum], '')

    options = [random.randint(0, len(f2content)-1),
        random.randint(0, len(f2content)-1),
        random.randint(0, len(f2content)-1)]

    options[random.randint(0, 2)] = wordnum

    print ('A -', f2content[options[0]],)
    print ('B -', f2content[options[1]],)
    print ('C -', f2content[options[2]],)

    answer = input('\nInput Answer ')

    if(options[answer-1] == int(wordnum)):
        raw_input('\nYou chose correctly. Push enter to continue...')
        score = score + 1
    else:
        raw_input('\nYou chose incorrectly. Push enter to continue...')

    count = count + 1

print('\nYour number correct is:', score)