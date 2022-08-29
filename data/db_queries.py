import sqlite3
import sqlalchemy
import os
from sqlalchemy.orm import sessionmaker
from data.models import *


class Db:
    def __init__(self, **connect_info):
        self.connect_info = connect_info
        dsn = f'sqlite:///../{self.connect_info["catalog"]}/{self.connect_info["base_name"]}'
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


info = {'catalog': 'database',
        'base_name': 'db_child.sqlite'}

new = Db(**info)
new.create_tab()

courses = [{'name': 'python для новичков',
            'min_age': 13,
            'max_age': 17,
            'description': 'Программирование на питоне'},
           {'name': 'кодвардс',
            'min_age': 9,
            'max_age': 11,
            'description': 'Основы программирования на кодвардсе'
            },
           {'name': 'Сиситемное администрированние',
            'min_age': 13,
            'max_age': 17,
            'description': 'Собираем компы и тд'
            }]

mentors = [{
    'firsname': 'Иван',
    'lastname': 'Иванов',
    'diplom': 'Красноярский педагогический'
},
    {
        'firsname': 'Светлана',
        'lastname': 'Иванова',
        'midlename': 'Петровна',
        'diplom': 'Красноярский технический'
    }]

for i in courses:
    new.add_directories(i)

for notes in mentors:
    new.add_mentors(notes)
