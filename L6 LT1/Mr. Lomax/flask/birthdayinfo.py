from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

def calc_next_birthday(dob):
    today = datetime.date.today()
    dob = dob

    birthday_this_year = datetime.date(today.year, dob.month, dob.day)
    birthday_next_year = datetime.date(today.year+1, dob.month, dob.day)

    if birthday_this_year > today:
        next_birthday = birthday_this_year
    else:
        next_birthday = birthday_next_year

    days_to_birthday = (next_birthday - today).days
    age = (next_birthday - dob).days // 365     # Note, this doesn't take account of leap years so isn't perfect.


    return today, dob, birthday_this_year, birthday_next_year, age, days_to_birthday, next_birthday

@app.route('/')
@app.route('/getname', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        dob = request.form['date']
        dob = datetime.date.fromisoformat(dob)
        today, dob, birthday_this_year, birthday_next_year, age, days_to_birthday, next_birthday = calc_next_birthday(dob)

    else:
        dob = datetime.datetime.today()


    return render_template('birthdayinfo.html', today=today, dob=dob, birthday_this_year=birthday_this_year, birthday_next_year=birthday_next_year, age=age, days_to_birthday=days_to_birthday, next_birthday=next_birthday)



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=80, debug=True)