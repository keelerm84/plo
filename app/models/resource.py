from app import db


class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    link = db.Column(db.String)
    description = db.Column(db.String)

    def to_dict(self):
        return dict(
            title=self.title,
            link=self.link,
            description=self.description,
            id=self.id
        )

    def __repr__(self):
        return '<Resource %r>' % (self.id)
