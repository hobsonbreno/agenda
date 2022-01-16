# Metodos e funções ultilizadas no cad agenda.

from datetime import datetime
from os import system
from time import sleep

def datahora():
	data = datetime.now().strftime('%d-%m-%Y - %H:%M')
	return data
	
def msntempo(temp, msn, titulo):
	i = 0
	while i <= 4:
		aguarde = ['Aguarde','Aguarde.','Aguarde..','Aguarde...','Aguarde....']
		system('cls')
		print('#'*15,'|',titulo,'|',datahora(),'|','#'*15)
		print('#'*5,'Notificação:',msn,aguarde[i])
		sleep(temp)
		i = i + 1
	system('cls')

def zeropro():
	print('Não há agenda cadastrados!'.center(77))
	print('cadastre uma agenda.'.center(77)) 

def atualizarzero():
	system('cls')
	print('#'*15,'| AGENDA TELEFONICA |',datahora(),'|','#'*15)
	print('#'*5,'Notificação: Não sabe o ID da agenda? Volte ao inicio e pesquise.')
	print('----------------------| Atualizar agenda existente |------------------------')
	print('Não há agenda cadastrados!'.center(77))
	print('Portanto não há o que atualizar.'.center(77))
	print('Retornando tela inicial'.center(77))
	print('-'*77)
	sleep(2) 
	msntempo(0.5,'Retornando tela inicial','CADASTRO DE AGENDA')

def removerzero():
	system('cls')
	print('#'*15,'| CADASTRO DE AGENDA |',datahora(),'|','#'*15)
	print('#'*5,'Notificação: Não sabe o ID da agenda? Volte ao inicio e pesquise.')
	print('------------------------| Remover agenda existente |------------------------')
	print('Não há agenda cadastrados!'.center(77))
	print('Portanto não há o que remover.'.center(77)) 
	print('Retornando tela inicial'.center(77))
	print('-'*77)
	sleep(2) 
	msntempo(0.5,'Retornando tela inicial','CADASTRO DE AGENDA')
	
