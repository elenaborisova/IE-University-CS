def main():
    print('This is a program that calculates quiz grade')

    quiz_score = int(input('Enter quiz score between 0 and 5: '))
    grade = '-'

    if quiz_score == 5:
        grade = 'A'
    elif quiz_score == 4:
        grade = 'B'
    elif quiz_score == 3:
        grade = 'C'
    elif quiz_score == 1 or quiz_score == 0:
        grade = 'F'
    else:
        print('Invalid quiz score.')

    print('Grade is:', grade)


main()
