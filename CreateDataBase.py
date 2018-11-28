from designist import db
from designist.model import Post,User,Category

if __name__ == '__main__':
    db.drop_all()
    db.create_all()