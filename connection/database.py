"""The database file"""
import os
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine, MetaData

load_dotenv(find_dotenv())

MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_DB = os.environ.get("MYSQL_DB")

DATABASE_URL = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@localhost:3306/{MYSQL_DB}'

engine = create_engine(DATABASE_URL)

metadata = MetaData()
