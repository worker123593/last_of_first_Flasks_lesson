from flask import Flask, url_for


app = Flask(__name__)


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                    <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
                        <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,700&display=swap" rel="stylesheet">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Пейзажи Марса</title>
                        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
                        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
                    </head>
                    
                    <body>
                        <h1>Пейзажи Марса</h1>
                        <div class="container">
                                <div id="carousel-basic" class="carousel" data-ride="carousel">
                                    <ol class="carousel-indicators">
                                        <li data-target="carousel-basic" data-slide-to="0" class="active"></li>
                                        <li data-target="carousel-basic" data-slide-to="1"></li>
                                        <li data-target="carousel-basic" data-slide-to="2"></li>
                                        <li data-target="carousel-basic" data-slide-to="3"></li>
                                    </ol>
                                    <div class="carousel-inner" role="listbox">
                                        <div class="carousel-item active">
                                            <img src="{url_for('static', filename='img/MARS.png')}" class="size" class="img-fluid">
                                        </div>
                                        <div class="carousel-item">
                                            <img src="{url_for('static', filename='img/MARS2.png')}" class="size" class="img-fluid">
                                        </div>
                                        <div class="carousel-item">
                                            <img src="{url_for('static', filename='img/MARS3.png')}" class="size" class="img-fluid">
                                        </div>
                                        <div class="carousel-item">
                                            <img src="{url_for('static', filename='img/MARS4.png')}" class="size" class="img-fluid">
                                        </div>
                                    </div>
                                    <a class="carousel-control-prev" href="#carousel-basic" role="button" data-slide="prev">
                                        <span class="carousel-control-prev-icon"></span>
                                        <span>Назад</span>
                                    </a>
                                    <a class="carousel-control-next" href="#carousel-basic" role="button" data-slide="next">
                                        <span>Вперед</span>
                                        <span class="carousel-control-next-icon" ></span>
                            
                                    </a>
                            </div>
                        </div>
                        </body>
                    </html>'''


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
