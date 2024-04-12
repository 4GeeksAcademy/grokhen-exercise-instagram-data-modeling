import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class User_Profile(Base):
    __tablename__ = 'user_profile'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    username = Column(String(250), nullable=False)
    nickname = Column(String(250), nullable=False)
    profile_description = Column(String(250), nullable=False)
    profile_picture = Column(String(250), ForeignKey('media.id'))
    user = relationship(User)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    media = Column(String(250), ForeignKey('media.id'))
    user_id = Column(Integer, ForeignKey('user_profile.user_id'))
    user = relationship(User_Profile)

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    post_id = Column(String(250), ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user_profile.user_id'))
    post = relationship(Post)
    comment = Column(String(250))

class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    post_id = Column(String(125), ForeignKey('post.id'))
    user_id = Column(String(125), ForeignKey('user_profile.user_id'))
    post = relationship(Post)

class Follows_Followers(Base):
    __tablename__ = 'follows_followers'
    id = Column(Integer, primary_key=True)
    follower = Column(String(125), ForeignKey('user_profile.user_id'))
    follow = Column(String(125), ForeignKey('user_profile.user_id'))
    user = relationship(User_Profile)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    media = Column(String(125))
    user_id = Column(String(125), ForeignKey('user_profile.user_id'))
    user = relationship(User_Profile)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
