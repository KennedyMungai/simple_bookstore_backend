"""The database file"""
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_DB = os.environ.get("MYSQL_DB")