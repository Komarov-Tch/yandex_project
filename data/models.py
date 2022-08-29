import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Child(Base):
    """Информация о студенте"""
    __tablename__ = 'child'

    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    name = sq.Column(sq.Text, nullable=False)
    surname = sq.Column(sq.Text, nullable=False)
    date_of_birth = sq.Column(sq.DateTime, nullable=False)
    id_shool = sq.Column(sq.Text, sq.ForeignKey('shool.id'), nullable=False)
    id_group = sq.Column(sq.Integer, sq.ForeignKey('group.id'), nullable=True)
    class_num = sq.Column(sq.Text, nullable=False)
    telephone = sq.Column(sq.Text, nullable=True)
    shool = relationship('Shool', backref='child')
    group = relationship('Group', backref='child')


class Shool(Base):
    """Школа где ребенок учится"""
    __tablename__ = 'shool'

    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    name = sq.Column(sq.Text, nullable=False)
    adress = sq.Column(sq.Text, nullable=False)
    director = sq.Column(sq.Text, nullable=False)
    telephone = sq.Column(sq.Text, nullable=False)


class Group(Base):
    """Группа"""
    __tablename__ = 'group'

    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    code = sq.Column(sq.Text, unique=True, nullable=False)
    id_mentors = sq.Column(sq.Integer, sq.ForeignKey('mentor.id'), nullable=False)
    id_direction = sq.Column(sq.Integer, sq.ForeignKey('directories.id'), nullable=False)
    mentor = relationship('Mentor', backref='group')
    directories = relationship('Directories', backref='group')


class Mentor(Base):
    """Преподаватели"""
    __tablename__ = 'mentor'

    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    firsname = sq.Column(sq.Text, nullable=False)
    lastname = sq.Column(sq.Text, nullable=False)
    midlename = sq.Column(sq.Text, nullable=True)
    diplom = sq.Column(sq.Text, nullable=False)


class Directories(Base):
    """Направления образования"""
    __tablename__ = 'directories'

    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    name = sq.Column(sq.Text, nullable=False)
    min_age = sq.Column(sq.Integer, nullable=False)
    max_age = sq.Column(sq.Integer, nullable=False)
    description = sq.Column(sq.Text, nullable=True)


class Parents(Base):
    """Родители ребенка"""
    __tablename__ = 'parents'
    id = sq.Column(sq.Integer, primary_key=True, unique=True, autoincrement=True)
    name = sq.Column(sq.Text, nullable=False)
    surname = sq.Column(sq.Text, nullable=False)
    id_child = sq.Column(sq.Text, sq.ForeignKey('child.id'), nullable=False)
    child = relationship('Child', backref='parents')


def create_table(engine):
    try:
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        return True
    except:
        return False
