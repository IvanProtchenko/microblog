from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine
engine = create_engine('sqlite:////work/python/migrate_sql_goog/app.db', echo=True)

metadata = MetaData()
users_table = Table('wiki_users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)), # Для некоторых БД не нужно указывать размер полей VARCHAR. Для mysql - обязательно.
    Column('fullname', String(50)),
    Column('password', String(50))
)
metadata.create_all(engine)
