from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from camera import take_photo, build_command

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
from models import ImageStore


@app.route("/", methods=['GET', 'POST'])
def land():
    query = ImageStore.query.order_by('-id').first()
    if query != "":
        filename = query.filename
        print filename
    else:
        filename = "test.jpg"
    return render_template('main.html', filename=filename)


@app.route("/shutter")
def shutter():
    ss = request.args.get('shutter_speed')
    wb = request.args.get('white_balance')
    # Get the last image stored to the database;
    query = ImageStore.query.order_by('-id').first()
    # If this query exists, increment its id
    # and use it to name the next file
    if query is not None:
        next_id = query.id + 1
        name = "snap" + str(next_id) + ".jpg"
    else:
        name = "snapX"
    # build camera command with variables and send to camera
    take_photo(build_command(name, ss, wb))
    # Add new photo info to database:
    session = db.session()
    img = ImageStore()
    img.filename = name
    session.add(img)
    session.commit()
    return name


if __name__ == "__main__":
    app.run()
