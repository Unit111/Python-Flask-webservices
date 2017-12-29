from app import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    # def to_json(self):
    #     return dict(id=self.id,
    #                 username=self.username,
    #                 email=self.email)


class Tasks(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    description = db.Column(db.String(128))
    done = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Tasks {}>'.format(self.body)