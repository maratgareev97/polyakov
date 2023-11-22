from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Замените это на случайную строку

login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id


# Замените этот словарь на базу данных или другой способ хранения пользователей
users = {'1': {'username': 'u', 'password': 'p'}}


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_id = None

        # Поиск пользователя в словаре (в реальном приложении замените на запрос к базе данных)
        for uid, user in users.items():
            print(uid,user)
            if user['username'] == username and user['password'] == password:
                user_id = uid
                break

        if user_id:
            user = User(user_id)
            login_user(user)
            return redirect(url_for('dashboard'))

    return render_template('login.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return f'Привет, {current_user.id}! Это ваша защищенная страница.'


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Вы успешно вышли.'

@app.route('/all')
def all():
    return "Могут все заходить"


if __name__ == '__main__':
    app.run(debug=True)
