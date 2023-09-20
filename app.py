from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY") or os.urandom(24)
oauth = OAuth(app)
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", None)


@app.route("/")
def home():
    if session and 'user' in session and session['user'] != None:
        # records = get_records(session['user']['email'])
        return render_template('index.html')
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

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    app.run(debug=True, host='0.0.0.0', port=port)


