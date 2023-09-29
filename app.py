from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os
from authlib.integrations.flask_client import OAuth
from authlib.common.security import generate_token
from urllib.parse import unquote

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY") or os.urandom(24)
oauth = OAuth(app)
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", None)
from controllers import create_record, get_records, update_vote, insert_comment, get_comments

@app.route("/")
def home():
    if session and 'user' in session and session['user'] != None:
        records = get_records()
        name = session['user']['name']
        # records = get_records(session['user']['email'])
        return render_template('index.html', records = records, name=name)
    else:
        app.logger.info('Need to log in')
        return render_template('login.html')

@app.route('/google/')
def google():
    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )
    redirect_uri = url_for('google_auth', _external=True)
    # print(redirect_uri)
    session['nonce'] = generate_token()
    return oauth.google.authorize_redirect(redirect_uri, nonce=session['nonce'])

@app.route('/google/auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token, nonce=session['nonce'])
    session['user'] = user
    app.logger.info('Update session info for user')
    return redirect('/')

@app.route("/logout")
def logout():
    if 'user' in session:  
        session.pop('user',None)  
    if 'nonce' in session:
        session.pop('nonce', None)  
    app.logger.info('Logging out')
    return redirect('/')

@app.route("/add_record", methods=['GET', 'POST'])
def add_record():
    email = session['user']['email']
    anime_name = request.args.get('anime_name')
    character_1, character_2 = request.args.get('character_1'), request.args.get('character_2')
    if character_1 and character_2:
        create_record(character_1, character_2, anime_name, email)
    else:
        print("invalid submission")
    return redirect('/')

@app.route("/vote", methods=['GET', 'POST'])
def vote():
    if request.method == 'POST':
        id = request.args.get('id')
        character = request.args.get('character')
        update_vote(id, character)
    return redirect('/')

@app.route("/add_comment", methods=['GET', 'POST'])
def add_comment():
    if request.method == "POST":
        email = session['user']['email']
        clicked=request.get_json('data')
        # print("clicked", clicked)
        clicked = clicked.split("=")
        # comment = clicked[1]
        comment = unquote(clicked[1])
        print("comment", comment)
        div_id = clicked[0]
        id = div_id.split("_")[1]
        # print("id", id)
        insert_comment(email, comment, id)
        return jsonify({'id': id})
    
@app.route("/show_comments", methods=['GET', 'POST'])
def show_comments():
    print("is this being called")
    if request.method == "POST":
        id=request.get_json('data')
        # print("id", id)
        comments = get_comments(id)
        return jsonify({'id': id,'data': render_template('comments.html', comments=comments)})

@app.route("/comment", methods=['GET', 'POST'])
def comment():
    if request.method == 'POST':
        email = session['user']['email']
        id = request.args.get('id')
        specific_comment = 'comment_'+id
        # print("specific_comment", specific_comment)
        comment = request.form.get(specific_comment)
        insert_comment(email, comment, id)
    return redirect('/')



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, host='localhost', port=port)



