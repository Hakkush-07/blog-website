from datetime import datetime
from blog import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(20), nullable=False, default="Hakkush")
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
