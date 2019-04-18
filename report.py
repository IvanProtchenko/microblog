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


'''
#чтение документа

range_name = 'list1!A:D'
table = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=range_name).execute()
print(table)

#обновление документа
cell='A1'
list_title='list1'
service.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheetId, 
body = {
"valueInputOption": "USER_ENTERED",
"data": [
    {"range": list_title + "!" + cell,
     "majorDimension": "ROWS",
     "values": [['вставка1','вставка2','вставка3'],['z1','z2','z3','z4']]}

]
}).execute()

#очистка документа
service.spreadsheets().values().clear(spreadsheetId=spreadsheetId,range=range_name).execute()
'''
