# import packages
from turtle import title
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config, DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)


# tags
tags = db.Table(
  'post_tags',
  db.Column('post_id', db.Integer, db.ForeignKey('user_posts.id')),
  db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)

# user's model
class User(db.Model):
  __tablename__ = 'user_table_name'

  id = db.Column(db.Integer(), primary_key=True)
  username = db.Column(db.String(255))
  password = db.Column(db.String(255))
  posts = db.relationship(
    'Post',
    backref='user',
    lazy='dynamic'
  )

  def __init__(self, username):
    self.username = username

  def __repr__(self):
    return "<User '{}'>".format(self.username)


# post model
class Post(db.Model):
  __tablename__ = 'user_posts'

  id = db.Column(db.Integer(), primary_key=True)
  title = db.Column(db.String(255))
  text = db.Column(db.Text())
  publish_date = db.Column(db.DateTime())

  # comment adding
  comments = db.relationship(
    'Comment',
    backref='post',
    lazy='dynamic'
  )

  user_id = db.Column(db.Integer(), db.ForeignKey('user_table_name.id'))

  # tags adding
  tags = db.relationship(
    'Tag',
    secondary=tags,
    backref=db.backref('posts', lazy='dynamic')
  )


  def __init__(self, title):
    self.title = title

  def __repr__(self) -> str:
    return "<Post '{}'>".format(self.title)


# comment model
class Comment(db.Model):
  __tablename__ = 'post_comments'

  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(255))
  text = db.Column(db.Text())
  date = db.Column(db.DateTime())
  post_id = db.Column(db.Integer(), db.ForeignKey('user_posts.id'))

  def __repr__(self):
    return "<Comment '{}>".format(self.text[:15])


# tag model
class Tag(db.Model):
  __tablename__ = 'tag_comment'

  id = db.Column(db.Integer(), primary_key=True)
  title = db.Column(db.String(255))

  def __init__(self, title):
    self.title = title

  def __repr__(self):
    return "<Tag '{}'>".format(self.title)


@app.route('/')
def home():
  return '<h1>Hello World!</h1>'


if __name__ == '__main__':
  app.run()
