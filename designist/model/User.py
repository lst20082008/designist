from designist import db

collections = db.Table('collections',
    db.Column('post_id',db.Integer,db.ForeignKey('post.id'),primary_key=True), 
    db.Column('user_id',db.Integer,db.ForeignKey('user.id'),primary_key=True)
)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50),unique=True,nullable=False)
    password = db.Column(db.String(200),nullable=False)
    telphone = db.Column(db.String(20))
    email = db.Column(db.String(50))
    image = db.Column(db.String(50))
    collections = db.relationship('Post',secondary=collections,lazy='subquery',backref=db.backref('users',lazy=True))

    def __init__(self,username,password,telphone,email):
        self.username  = username
        self.password = password
        self.telphone = telphone
        self.email = email
        self.image = 'user_default.jpg'
    def __repr__(self):
        return '<User %r>' % self.username