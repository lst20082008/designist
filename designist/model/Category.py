from designist import db

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),unique=True,nullable=False)
    father_id = db.Column(db.Integer)
    post = db.relationship('Post',backref='category',lazy=True)

    def __init__(self,name,father_id):
        self.name  = name
        self.father_id = father_id
    def __repr__(self):
        return '<Category %r>' % self.name