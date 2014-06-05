from picam import db


class ImageStore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.Integer)
    date = db.Column(db.String(30))

    def __repr__(self):
        return "<Image(id={id}, filename={filename}, date={date}"\
            .format(id=self.id, filename=self.filename, date=self.date)
