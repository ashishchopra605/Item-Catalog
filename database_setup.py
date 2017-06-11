from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.mysql import VARCHAR, TEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Category(Base):
    __tablename__ = 'news_category'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    imgurl = Column(String(250), nullable=False)
    description = Column(TEXT)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref="category")

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class News(Base):
    __tablename__ = 'news'

    heading = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    imgurl = Column(String(250), nullable=False)
    description = Column(TEXT)
    category_id = Column(Integer, ForeignKey('news_category.id'))
    category = relationship(Category, backref=backref("items", cascade="all, delete-orphan"))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref="items")

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'heading': self.heading,
            'description': self.description,
            'id': self.id
        }


engine = create_engine('sqlite:///newswebapplication.db')


Base.metadata.create_all(engine)
