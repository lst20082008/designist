from designist import db
import datetime

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    abstract = db.Column(db.Text)
    image = db.Column(db.String(50))
    content = db.Column(db.Text,nullable=False)
    date = db.Column(db.DateTime,nullable=False)
    likes = db.Column(db.Integer)
    reads = db.Column(db.Integer)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'),nullable=False)

    def __init__(self,title,abstract,content,category_id):
        self.title  = title
        self.abstract = abstract
        self.content = content
        self.date = datetime.datetime.now()
        self.category_id = category_id
        self.image = 'post_'+title+'.jpg'
        self.likes = 0
        self.reads = 0
    def __repr__(self):
        return '<Post %r>' % self.title