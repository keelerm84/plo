from app import db
import markdown


class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    story = db.Column(db.String)
    photo_path = db.Column(db.String)

    def to_dict(self):
        return dict(
            first_name=self.first_name,
            story=markdown.markdown(self.story),
            photo_path=self.photo_path,
            id=self.id
        )

    def __repr__(self):
        return '<Testimonial %r>' % (self.id)
