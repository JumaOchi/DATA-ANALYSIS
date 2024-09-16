from flask import Flask, render_template
from api import create_app

app = create_app()

@app.route('/')
def dashboard():
    return render_template('template/dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
