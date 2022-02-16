from website import create_app

app = create_app()

if __name__ == '__main__':
    #todo: FLEX-3 - set debug to false in production
    app.run(debug=True)
