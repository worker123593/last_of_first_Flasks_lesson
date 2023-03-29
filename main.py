from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def mission():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def add():
    return """<p>Человечество вырастает из детства.</p>
        <p>Человечеству мала одна планета.</p>
        <p>Мы сделаем обитаемыми безжизненные пока планеты.</p>
        <p>И начнем с Марса!</p>
        <p>Присоединяйся!</p>"""


@app.route('/image_mars')
def third_num():
    return f"""<html>
    <head><tile>Привет, Марс!</tile></head>
    <body>
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='img/MARS.png')}" alt="здесь должна была быть картинка, но не нашлась">
    <p>Вот она какая, красная планета</p>
    </body></html>"""


@app.route('/promotion_image')
def fourth_num():
    return f"""<html>
    <head>
        <tile>Привет, Марс!</tile>
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    </head>
    <body>
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='img/MARS.png')}" alt="здесь должна была быть картинка, но не нашлась">
    <p class="alert alert-secondary" role="alert">Человечество вырастает из детства.</p>
    <p class="alert alert-primary" role="alert">Человечеству мала одна планета.</p>
    <p class="alert alert-warning" role="alert"> Мы сделаем обитаемыми безжизненные пока планеты.</p>
    <p class="alert alert-success" role="alert">И начнем с Марса!</p>
    <p class="alert alert-danger" role="alert">Присоединяйся!</p>
    </body></html>"""


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')