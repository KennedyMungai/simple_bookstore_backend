"""Created the model file for the books data"""
from sqlalchemy import Column, Integer, String, Table

from connection.database import metadata

books = Table(
    "books",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("Author", String)
)
