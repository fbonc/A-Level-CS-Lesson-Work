from flask import Flask
from flask import request
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is a website!'

@app.route('/add')
def add():
    first_number = request.args.get('first', '')
    second_number = request.args.get('second', '')
    if first_number and second_number:
        try:
            result = int(first_number) + int(second_number)
        except ValueError:
            return 'Invalid data'
        return f'{first_number} + {second_number} = {result}'
    else:
        return 'No arguments detected'

@app.route('/birthday')
def calc_next_birthday():
    today = datetime.date.today()

    dob = request.args.get('dob', '')
    dob = dob.split('-')
    dob = datetime.date(int(dob[0]), int(dob[1]), int(dob[2]))

    print("My date of birth is: ", dob)
    print("Today is: ", today)
    birthday_this_year = datetime.date(today.year, dob.month, dob.day)
    birthday_next_year = datetime.date(today.year+1, dob.month, dob.day)

    if birthday_this_year > today:
        next_birthday = birthday_this_year
    else:
        next_birthday = birthday_next_year

    print('Next birthday: ', next_birthday)
    days_to_birthday = (next_birthday - today).days
    age = (next_birthday - dob).days // 365     # Note, this doesn't take account of leap years so isn't perfect.
    print('Days to next birthday: ', days_to_birthday)
    print('Age at next birthday: ', age)

    return f"\
    <style>h1, p {{text-align: center}} body {{background-color: lightblue;}}</style>\
    <h1>Birthday Information</h1>\
    <p>My date of birth is: {dob}</p>\
    <p>Today is: {today}</p>\
    <p>Next Birthday: {next_birthday}</p>\
    <p>Days to next birthday: {days_to_birthday}</p>\
    <p>Age at next birthday {age}</p>"


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=80, debug=True)