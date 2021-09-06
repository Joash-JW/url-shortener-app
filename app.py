from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import urlparse
from random import choice
import string, logging

app = Flask(__name__, template_folder='./frontend', static_folder='./frontend')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # comment out when deploy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tuzhmmegshfmyv:c4a1cfa40a3b3eb182adaa3616137bceeb613fe5331b575fa861d2d6d4624a9f@ec2-44-196-8-220.compute-1.amazonaws.com:5432/d4n89ir995sblm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class UrlMapping(db.Model):
    shortUrl = db.Column(db.String(6), primary_key=True)
    longUrl = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return '<UrlMapping %r %r>' %(self.shortUrl, self.longUrl)

# endpoints
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shortenUrl():
    if request.method == 'POST' and checkUrlFormat(request.form['longUrl']):
        short_endpoint = generateShortEndpoint()
        newUrlMapping = UrlMapping(shortUrl=short_endpoint, longUrl=request.form['longUrl'])
        try:
            log.info('Mapping created: {/'+short_endpoint+' : '+request.form['longUrl']+'}')
        except NameError:
            pass
        db.session.add(newUrlMapping)
        db.session.commit()
        return request.url_root+short_endpoint
    return redirect('/')

@app.route('/<short_endpoint>', methods=['GET'])
def goToUrl(short_endpoint):
    queryResult = UrlMapping.query.filter(UrlMapping.shortUrl==short_endpoint).first()
    if (queryResult):
        return redirect(queryResult.longUrl)
    else:
        return redirect('/')

def checkUrlFormat(longUrl):
    try:
        result = urlparse(longUrl)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def generateShortEndpoint(length=6):
    while True:
        short_endpoint = ''.join(choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length))
        queryResult = UrlMapping.query.filter(UrlMapping.shortUrl==short_endpoint).first()
        if not queryResult:
            break
    return short_endpoint

if __name__ == '__main__':
    log = logging.getLogger("logger")
    logging.basicConfig(level = logging.INFO)

    # db.drop_all() # reset database
    # db.create_all() # comment out when deploy
    # print(UrlMapping.query.all())
    app.run()