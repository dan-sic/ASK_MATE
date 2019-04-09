from flask import Flask
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__, template_folder='../templates', static_folder='../static')
photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/images'
# prevent catching files in browser:
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
configure_uploads(app, photos)
