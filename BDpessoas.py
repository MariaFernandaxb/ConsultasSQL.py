import sqlite3

conexao = sqlite3.connect('exercicio.db')
cursor =  conexao.cursor()


cursor.execute('''
CREATE TABLE PESSOAS (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    NOME TEXT(100),
    IDADE INTEGER,
    CIDADE TEXT(30)
)'''
)

cursor.execute('''
CREATE TABLE HOBBIES (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    PESSOA_ID INTEGER NOT NULL,
    HOBBY TEXT(40),
    FOREIGN KEY (PESSOA_ID) REFERENCES PESSOAS(ID)
)'''
)

conexao.commit()
conexao.close()