from orm.builder.attributes import ColumnAttribute
from orm.declarative.base import TableModel
from orm.crud.insert import Insert
from orm.crud.select import Select
from orm.crud.update import Update



class User(TableModel):
    __tablename__ = 'TB_USER'
    id = ColumnAttribute('INTEGER', primary_key=True, not_null=True)
    nome = ColumnAttribute('VARCHAR(40)')
    id_address = ColumnAttribute('INTEGER')

class Address(TableModel):
    id = ColumnAttribute('INTEGER', primary_key=True, not_null=True)
    nome = ColumnAttribute('VARCHAR(40)')


sql = Select(User,'').filter(User.id != 0).join(Address,[User.id_address == Address.id])
sql2 = Insert(User,'').values(id=1,nome='Guilherme Duarte', id_address=1)
sql3 = Update(User,'').Set(nome='Guilherme Duarte').filter(User.id == 1)
print(sql)
print('-'*20)
print(sql2)
print('-'*20)
print(sql3)


