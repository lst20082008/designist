from designist import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50),unique=True,nullable=False)
    password = db.Column(db.String(200),nullable=False)
    telphone = db.Column(db.String(20))
    email = db.Column(db.String(50))

    def __init__(self,username,password,telphone,email):
        self.username  = username
        self.password = password
        self.telphone = telphone
        self.email = email
    def __repr__(self):
        return '<User %r>' % self.username