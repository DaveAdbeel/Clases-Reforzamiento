from flask import Flask, render_template
from models.users import Users

app = Flask(__name__)

@app.route('/')
def index():
    users = Users.get_all()    
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)