from app import create_crud

app = create_crud()

if __name__ == "__main__":
    app.run(debug=True)