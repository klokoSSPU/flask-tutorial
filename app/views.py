def index():
    user = {'nickname': 'Jakub'}
    posts = [
        { 
            'author': {'nickname': 'Anonym'},
            'body': 'Dnes je v Opave pekne!'
        },
        { 
            'author': {'nickname': 'Pocasi'},
            'body': 'You dont say'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)