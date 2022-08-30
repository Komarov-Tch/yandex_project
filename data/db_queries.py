import sqlite3
import sqlalchemy
import os
from sqlalchemy.orm import sessionmaker
from models import *


class Db:
    def __init__(self, base_name):
        dsn = f'sqlite:///{base_name}'
        self.engine = sqlalchemy.create_engine(dsn)

    def return_engine(self):
        return self.engine

    def create_tab(self):
        create_table(self.engine)

    def add_child(self, child_info: dict) -> bool:
        ...

    def add_directories(self, courese_info: dict) -> bool:
        """

        :param courese_info:
        name:str
        min_age:int
        max_age:int
        description:str
        :return: true or false
        """
        try:
            Session = sessionmaker(bind=self.engine)
            session = Session()
            add_ = Directories(**courese_info)
            session.add(add_)
            session.commit()
            session.close()
            return True
        except:
            return False

    def add_mentors(self, mentor_info: dict) -> bool:
        """
        adding teachers
        :param mentor_info:
        name:str
        dilom:str
        :return:
        """
        try:
            Session = sessionmaker(bind=self.engine)
            session = Session()
            add_ = Mentor(**mentor_info)
            session.add(add_)
            session.commit()
            session.close()
            return True
        except:
            return False

    def add_school(self, shool_info: dict) -> bool:
        """
        adding information about the school
        :param shool_info:
        title:str
        adress:str
        diretor:str
        telephone:str
        :return: bool
        """
        try:
            Session = sessionmaker(bind=self.engine)
            session = Session()
            add_ = Shool(**shool_info)
            session.add(add_)
            session.commit()
            session.close()
            return True
        except:
            return False

    def add_group(self, group_info: dict) -> bool:
        """
        :param group_info:
        :firstname  - mentor
        :lastname - mentor
        :code: number of group
        :title - title Direrories
        :return:
        """
        try:
            Session = sessionmaker(bind=self.engine)
            session = Session()
            query_m = self.query_mentor(group_info['firstname'], group_info['lastname'])
            if query_m:
                id_mentor = query_m[0]['id']
            else:
                raise
            query_d = self.query_directories(group_info['title'])
            if query_d:
                id_derictories = query_d[0]['id']
            else:
                raise
            add_ = Group(code=group_info['code'],
                         id_mentors=id_mentor,
                         id_direction=id_derictories)
            session.add(add_)
            session.commit()
            session.close()
            return True
        except:
            return False

    def query_mentor(self, firstname, lastname) -> list:
        Session = sessionmaker(bind=self.engine)
        session = Session()
        query = session.query(Mentor).filter(Mentor.firstname == firstname, Mentor.lastname == lastname).all()
        session.close()
        result = []
        for q in query:
            result.append({'id': q.id,
                           'firstname': q.firstname,
                           'lastname': q.lastname,
                           'midlename': q.midlename,
                           'diplom': q.diplom})
        return result

    def query_directories(self, title: str) -> list:
        Session = sessionmaker(bind=self.engine)
        session = Session()
        query = session.query(Directories).filter(Directories.title == title).all()
        session.close()
        result = []
        for q in query:
            result.append({'id': q.id,
                           'title': q.title,
                           'min_age': q.min_age,
                           'max_age': q.max_age,
                           'description': q.description})
        return result


info = 'db_child.sqlite'

new = Db(info)
new.create_tab()

courses = [{'title': 'python для новичков',
            'min_age': 13,
            'max_age': 17,
            'description': 'Программирование на питоне'},
           {'title': 'кодвардс',
            'min_age': 9,
            'max_age': 11,
            'description': 'Основы программирования на кодвардсе'
            },
           {'title': 'Сиситемное администрированние',
            'min_age': 13,
            'max_age': 17,
            'description': 'Собираем компы и тд'
            }]

mentors = [{
    'firstname': 'Иван',
    'lastname': 'Иванов',
    'diplom': 'Красноярский педагогический'
},
    {
        'firstname': 'Светлана',
        'lastname': 'Иванова',
        'midlename': 'Петровна',
        'diplom': 'Красноярский технический'
    }]

group_info = {'firstname': 'Иван',
              'lastname': 'Иванов',
              'code': 'cod-22-01',
              'title': 'кодвардс'}
for i in courses:
    new.add_directories(i)

for notes in mentors:
    new.add_mentors(notes)

print(new.add_group(group_info))
