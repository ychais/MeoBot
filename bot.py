def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input('3: '))
    rem5 = int(input('5: '))
    rem7 = int(input('7: '))
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start learning!")


def count():
    print('Now I will prove to you that I can count to any number you want. Go on: ')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your knowledge.")
    print('What African country served as the setting for Tatooine in Star Wars?')
    right_answer = [3]
    print('1. Gabon')
    print('2. Tunisia')
    print('3. Ghana')
    print('4. Ethiopia')

    # part of code without loop in case of a wrong answer:
    # user_answer = input('Your answer: ')
    # if user_answer in right_answer:
    #     return 'Completed, have a nice day!'
    # else:
    #     user_answer = (str(input('Please, try again')))

    while True:
        user_answer = int(input())
        if user_answer not in right_answer:
            print('Please, try again ')

        else:
            print('Completed, have a nice day!')
            break


def end():
    print('Congratulations, have a nice day!')


greet('Meo', '2021')
remind_name()
guess_age()
count()
test()
end()
