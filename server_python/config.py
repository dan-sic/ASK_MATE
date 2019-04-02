from flask import Flask
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__, template_folder='../templates')
photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/images'
configure_uploads(app, photos)
