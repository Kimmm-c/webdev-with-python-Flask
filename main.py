# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def my_():
    return render_template('index.html')

@app.route("/<page_name>")
def blog(page_name):
    return render_template(page_name + '.html')

@app.route("/submit_form", methods=['POST', "GET"])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return data
        except:
            return 'did not save to db'
    else:
        return 'ecccc'

def write_to_file(data):
    #mode='a' -- to append
    with open('database.txt', mode='a') as database:
        email = data['email']
        name = data['name']
        message = data['message']
        file = database.write(f'\n{email}, {name}, {message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data['email']
        name = data['name']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='`', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, name, message])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
