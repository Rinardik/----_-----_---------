from flask import Flask, request, url_for, redirect, render_template
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"


class LoginForm(FlaskForm):
    id_astr = StringField('id астронавта', validators=[DataRequired()])
    password_astr = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_kap = StringField('id капитана', validators=[DataRequired()])  # Исправлено название поля
    password_kap = PasswordField('Пароль капитана', validators=[DataRequired()])  # Исправлено название поля
    submit = SubmitField('Доступ')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/table')
def table():
    gender = request.args.get('gender', '')
    age_str = request.args.get('age', '0')
    try:
        age = int(age_str)
    except ValueError:
        age = 0
    return render_template('training.html', gender=gender, age=age)

@app.route('/selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('selection_form.html')  # Лучше вынести форму в отдельный шаблон
    
    elif request.method == 'POST':
        surname = request.form.get('surname', 'Не указано')
        name = request.form.get('name', 'Не указано')
        email = request.form.get('email', 'Не указано')
        education = request.form.get('education', 'Не указано')
        professions = request.form.getlist('professions')
        sex = request.form.get('sex', 'Не указано')
        motivation = request.form.get('motivation', 'Не указано')
        photo = request.files.get('photo')
        stay_on_mars = 'stay_on_mars' in request.form

        return render_template('selection_result.html', 
                             surname=surname,
                             name=name,
                             email=email,
                             education=education,
                             professions=professions,
                             sex=sex,
                             motivation=motivation,
                             stay_on_mars=stay_on_mars)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')