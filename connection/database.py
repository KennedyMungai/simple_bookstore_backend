"""The database file"""
import os
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine, MetaData

load_dotenv(find_dotenv())

MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_DB = os.environ.get("MYSQL_DB")
MYSQL_HOST = os.environ.get("MYSQL_HOST")
MYSQL_PORT = os.environ.get("MYSQL_PORT")

DATABASE_URL = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}'

metadata = MetaData()

engine = create_engine(DATABASE_URL)

conn = engine.connect()

