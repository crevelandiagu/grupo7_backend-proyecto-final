from app import app

# app = create_app()

if __name__ == "__main__":
    import threading

    def funcion_1():
        app.test_client().get('/stream')

    threading_emails = threading.Thread(target=funcion_1)
    threading_emails.start()
    app.run(port=3007, debug=True)
