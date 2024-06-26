from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {
    'john': 'password123',
    'jane': 'mypassword'
}


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('welcome', username=username))
        else:
            error = "Invalid username or password"
            return render_template('login.html', error=error)
    return render_template('login.html')


@app.route('/welcome/<username>')
def welcome(username):
    return render_template('welcome.html', username=username)


@app.route('/create_ad', methods=['GET', 'POST'])
def create_ad():
    if request.method == 'POST':
        # Spracovanie údajov z formulára (trasa, čas, podmienky)
        # Uložte inzerát do databázy
        return redirect(url_for('success'))
    return render_template('create_ad.html')

@app.route('/success')
def success():
    return 'Inzerát bol úspešne vytvorený!'


if __name__ == '__main__':
    app.run(debug=True)
