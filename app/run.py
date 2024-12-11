from settings.flask_app import create_app

# execucao do programa onde tem o host, port e se e debugavel

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)