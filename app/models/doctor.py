from app import db


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    title = db.Column(db.String)
    street = db.Column(db.String)
    city = db.Column(db.String)
    region = db.Column(db.String)
    postal_code = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def to_dict(self):
        return dict(
            name=self.name,
            title=self.title,
            street=self.street,
            city=self.city,
            region=self.region,
            postal_code=self.postal_code,
            latitude=self.latitude,
            longitude=self.longitude,
            id=self.id
        )

    def __repr__(self):
        return '<Doctor %r>' % (self.id)
