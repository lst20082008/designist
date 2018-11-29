from designist import db

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    abstract = db.Column(db.Text)
    image = db.Column(db.String(50))
    content = db.Column(db.Text,nullable=False)
    date = db.Column(db.DateTime,nullable=False)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'),nullable=False)

    def __init__(self,title,abstract,content,date,category_id):
        self.title  = title
        self.abstract = abstract
        self.content = content
        self.date = date
        self.category_id = category_id
        self.image = 'post_'+title+'.jpg'
    def __repr__(self):
        return '<User %r>' % self.title