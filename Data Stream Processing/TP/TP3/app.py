from flask import Flask, render_template, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder="template")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://mayo:mayo@mysql/users'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    family_name = db.Column(db.String(80), unique=False, nullable=False)
    first_name = db.Column(db.String(80), unique=False, nullable=False)

    def _init_(self, family_name, first_name) -> None:
        super().__init__()
        self.family_name = family_name
        self.first_name = first_name

@app.route('/')
def home():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/my_account/<name>')
def page_1(name=None):
    return render_template('page_1.html', name=name)

@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        family_name = request.form['family_name']
        first_name = request.form['first_name']
        new_user = User(family_name=family_name, first_name=first_name)
        db.session.add(new_user)
        db.session.commit()
    return redirect(url_for('hello_world'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, host='0.0.0.0', port=5000)