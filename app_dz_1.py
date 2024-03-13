from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    content = {
        "title": "Главная",
        "exercise": [
            'Задание №8',
            'Создать базовый шаблон для всего сайта, содержащий',
            'общие элементы дизайна (шапка, меню, подвал), и',
            'дочерние шаблоны для каждой отдельной страницы.',
            'Например, создать страницу "О нас" и "Контакты",',
            'используя базовый шаблон.',
            '',
            'Задание №9',
            'Создать базовый шаблон для интернет-магазина,',
            'содержащий общие элементы дизайна (шапка, меню,',
            'подвал), и дочерние шаблоны для страниц категорий',
            'товаров и отдельных товаров.',
            'Например, создать страницы "Одежда", "Обувь" и "Куртка",',
            'используя базовый шаблон.'
        ],
    }

    return render_template('index.html', **content)


@app.route('/about/')
def about():
    context = {'title': '"О нас"'}
    return render_template('about.html', **context)


@app.route('/contacts/')
def main():
    contacts = [
        {'name': 'Александр',
         'email': 'al_@mail.ru',
         'phone': '+7-987-444-654-32-10',
         },
        {'name': 'Матвей',
         'mail': 'matv@mail.ru',
         'phone': '+7-987-444-33-22',
         },
        {'name': 'Максим',
         'mail': 'max@mail.ru',
         'phone': '+7-903-333-33-33',
         },
    ]
    content = {
        'contacts': contacts,
        'title': 'Контакты',
    }
    return render_template('contacts.html', **content)


@app.route('/cloth/')
def cloth():
    content = {'title': 'Одежда'}
    return render_template('base_cloth.html', **content)


@app.route('/shoes/')
def shoes():
    data = [
        {'name': 'S1',
         'title': 'sport good to run',
         'color': 'pink',
         'price': '100.23',
         'img': "/static/image/товары/shoes/S1.png",
         },
        {'name': 'S1-white',
         'title': 'sport good to run',
         'color': 'white',
         'price': '210.32',
         'img': "/static/image/товары/shoes/S2-white.png",
         },
    ]
    context = {'title': 'Обувь',
               'data': data}
    return render_template('shoes.html', **context)


@app.route('/jacket/')
def jacket():
    data = [
        {'name': 'jacket red',
         'title': 'sport',
         'color': 'red',
         'price': '300.10',
         'img': "/static/image/товары/jacket/jacket-1.png",
         },
        {'name': 'jacket black',
         'title': 'jacket to moto',
         'color': 'black',
         'price': '512.23',
         'img': "/static/image/товары/jacket/jacket-2.png",
         },
    ]
    context = {'title': 'Куртка',
               'data': data}
    return render_template('jacket.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
