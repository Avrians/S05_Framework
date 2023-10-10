from flask import Flask, url_for

app = Flask(_name_)

@app.route("/") #http://127.0.0.1:5000
def index():
    tes ='fid'
    return f'''
    <a href="{url_for('user', username='fid')}"> World!</a>
    '''

@app.route("/home") #http://127.0.0.1:5000/home
def home():
    return "<h1>This is my home !</h1>"

@app.route('/user/<username>')
def user(username):
    # show the user profile for that user
    return f'My name is {username}'

# with app.test_request_context():
#     print(url_for('user', username='fid'))