import json
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


@app.route('/member')
def member():
    with open('static/json/members.json', 'rt', encoding='utf-8') as file:
        membersList = json.loads(file.read())
    return render_template('members.html', members=membersList)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
