from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    dbname='b1mxnbtfaytwhs4af34m',
    user='uwj8p4v8zuoeyv3iqlxg',
    password='Kh3N5D3JtxcCyJeXuUeeZVNCROL6Jo',
    host="b1mxnbtfaytwhs4af34m-postgresql.services.clever-cloud.com",
    port=50013
)

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


rides = [
    {'from_location': 'Bratislava', 'to_location': 'Košice', 'date': '2024-07-01'},
    {'from_location': 'Žilina', 'to_location': 'Banská Bystrica', 'date': '2024-07-02'}
]


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        from_location = request.form.get('from_location')
        to_location = request.form.get('to_location')
        filtered_rides = [ride for ride in rides if
                          from_location.lower() in ride['from_location'].lower() and
                          to_location.lower() in ride['to_location'].lower()]
        return render_template('search.html', rides=filtered_rides)
    return render_template('search.html', rides=rides)


@app.route('/about')
def about():
    about_info = about.query.first()
    return render_template('about.html', about_info=about_info)

if __name__ == '__main__':
    app.run(debug=True)
