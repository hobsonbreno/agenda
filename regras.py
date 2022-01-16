'''
Metodos e funções a serem usadas no cad 
contatos relacionado ao bd
'''
import sqlite3

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()

def criartabelacontatos():
	query = ''' create table if not exists contatos(
			id integer primary key autoincrement,
			nome varchar(50) not null,
			codigo varchar(4) not null,
			setor varchar(50) not null);
			'''
	cursor.execute(query)

def inseririd(nome,codigo,setor):
	query = """insert into contatos(
			nome, codigo, setor) 
			values(
			'{}', {}, '{}'
			)""".format(nome, codigo, setor)
	cursor.execute(query)
	conexao.commit()

def editarid(nome, vnome, codigo, vcodigo, setor, vsetor, ident):
	query = """
	update contatos set '{}'='{}','{}'='{}','{}'='{}' where id={}
	""".format(nome, vnome, codigo, vcodigo, setor, vsetor, ident)
	cursor.execute(query)
	conexao.commit()

def removerid(valor):
	query = 'delete from contatos where id={}'.format(valor)
	cursor.execute(query)
	conexao.commit()

def contar():
	query = 'select * from contatos;'
	cursor.execute(query)
	resultado = cursor.fetchall()
	quant = len(resultado)
	if len(resultado) > 0:
		return "{:0>2}".format(quant)
	else:
		return '00'

def selecionar():
	query = 'select * from contatos;'
	cursor.execute(query)
	resultado = cursor.fetchall()
	return resultado

def procurarid(valor):
	query = 'select * from contatos where id={}'.format(valor)
	cursor.execute(query)
	resultado = cursor.fetchall()
	return resultado

def atualizar():
	query = 'select * from contatos;'
	cursor.execute(query)
	
def limitar(indice):
	query = 'select * from contatos limit {}, 5'.format(indice)
	cursor.execute(query)
	resultado = cursor.fetchall()
	return resultado

def localizarnome(valor):
	query = "select * from contatos where nome like '{}%'".format(valor)
	cursor.execute(query)
	resultado = cursor.fetchall()
	return resultado


