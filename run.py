from app import create_app


app = create_app()

if __name__ == '__main__':

    with app.app_context():
        from app.seeds.initial_data import create_seeds
        create_seeds()

    app.run(port=5000, debug=True)