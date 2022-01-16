from auxiliar import *
from regras import *

criartabelacontatos()

msntempo(0.2,'Inicializando Programa.','CADASTRO DE CONTATOS')
msntempo(0.3,'Conectando o banco de dados.','CADASTRO DE CONTATOS')

paginacao = 'P'

menu = True
while menu:
	atualizar()
	system('cls')
	print('#'*15,'| CADASTRO DE CONTATOS |',datahora(),'|','#'*15)
	print('#'*5,'Notificação: Seja Bem Vindo(a)! (:D). E fique à vontade.')
	print('-----------------| Há um total de',contar(),'Contatos registrados |------------------')
	print('ID\tNome\t\t\t\tCódigo\t\tTipo de contatos')
	print('-'*77)
	if (len(selecionar()) > 0) and (paginacao == 'P'):
		tamanho = len(selecionar())
		vfinal = round(tamanho / 5)
		if (tamanho % 5) > 0:
			vfinal = vfinal + 1
		pagi = 1
		pagf = vfinal
		valor = 0
		campos = limitar(valor)
		for x in campos:
			print("{:0>4}\t{:<30}\t{:0>4}\t\t{}".format(x[0], x[1], x[2], x[3]))
	elif (len(selecionar()) > 0):
		campos = limitar(valor)
		for x in campos:
			print("{:0>4}\t{:<30}\t{:0>4}\t\t{}".format(x[0], x[1], x[2], x[3]))
	else:
		zeropro()
	print('-'*58,'[Página {:0>2} de {:0>2}]-'.format(pagi,pagf))
	print('[A]: Página Anterior\t\t[P]: Próxima página'.center(77))
	print('-'*77)
	print('[I]: Inserir contatos\t[E]: Editar contatos')
	print('[R]: Remover contatos\t[L]: Localizar contatos')
	print('[S]: Sair')
	print()

	option = True

	while option:
		opcao = input('Selecione uma opção > ')

		if opcao == 'A' or opcao == 'a':
			if paginacao == 'P':
				system('cls')
				print('#'*15,'| CADASTRO DE CONTATOS |',datahora(),'|','#'*15)
				print('#'*5,'Notificação: Atenção! [:(]')
				print('-'*77)
				print('-----------------------| Não existe página anterior |------------------------')
				print('-'*77)
				sleep(1)
				msntempo(0.4,'Retornando tela inicial','CADASTRO DE CONTATOS')
				option = False
			else:
				valor = valor - 5
				pagi = pagi - 1
				if pagi == 1:
					paginacao = 'P'
				option = False
			
		elif opcao == 'P' or opcao == 'p':
			if paginacao == 'U':
				system('cls')
				print('#'*15,'| CADASTRO DE CONTATOS |',datahora(),'|','#'*15)
				print('#'*5,'Notificação: Atenção! [:(]')
				print('-'*77)
				print('-----------------------| Não existe página posterior |-----------------------')
				print('-'*77)
				sleep(1)
				msntempo(0.4,'Retornando tela inicial','CADASTRO DE CONTATOS')
				option = False
			else:
				valor = valor + 5
				pagi = pagi + 1
				paginacao = 'M'
				if pagi == pagf:
					paginacao = 'U'
				option = False
				
		elif opcao == 'I' or opcao == 'i':
			system('cls')
			print('#'*15,'| CADASTRO DE CONTATOS |',datahora(),'|','#'*15)
			print('#'*5,'Notificação: Fique atentos aos dados. Cuidado para não errar.')
			print('-------------------------| Adicionar novo contato |--------------------------')
			nome = input('Nome: ')
			codigo = input('Código: ')
			print('----------| Setor |----------')
			print('[1]: Cônjugue\t[2]: Namorado(a)')
			print('[3]: Amigo(a)\t[4]: Família') 
			print('[5]: Trabalho\t[6]: Conhecido(a)')
			
			inserir = True

			while inserir:
				opcao = int(input('Selecione uma opção > '))

				if opcao == 1:
					setor = 'Cônjugue'
					inserir = False
					option = False
				elif opcao == 2:
					setor = 'Namorado'
					inserir = False
					option = False
				elif opcao == 3:
					setor = 'Amigo(a)'
					inserir = False
					option = False
				elif opcao == 4:
					setor = 'Família'
					inserir = False
					option = False
				elif opcao == 5:
					setor = 'Trabalho'
					inserir = False
					option = False
				elif opcao == 6:
					setor = 'Conhecido(a)'
					inserir = False
					option = False
				else:
					print('Opção inválida')
			
			inseririd(nome, codigo, setor)
			campos = localizarnome(nome) 
			system('cls')
			print('#'*15,'| CADASTRO DE CONTATOS |',datahora(),'|','#'*15)
			print('#'*5,'Notificação: Seja Bem Vindo(a)! (:D). E fique à vontade.')
			print('ID\tNome\t\t\t\tCódigo\t\tTipo de contatos')
			print('-'*77)
			print('---------------------| Contatos cadastrados com sucesso |----------------------')
			print('-'*77)
			for x in campos:
				print("{:0>4}\t{:<30}\t{:0>4}\t\t{}".format(x[0], x[1], x[2], x[3]))
			print('-'*77)
			sleep(1)
			msntempo(0.4,'Retornando tela inicial','CADASTRO DE CONTATOS')
	
		elif opcao == 'E' or opcao == 'e':
			if len(selecionar()) > 0:
				chance = 1
				tentativa = 4
				while chance <= tentativa:
					system('cls')
					print('#'*15,'| CADASTRO DE CONTATOS |',datahora(),'|','#'*15)
					print('#'*5,'Notificação: Não sabe o ID do contato? Volte ao inicio e pesquise.')
					print('----------------------| Atualizar contato existente |------------------------')
					print('Tentativa {} de {}...\t [V]: Voltar ao inicio'.format(chance,tentativa).center(77))
					texto = input('Informe o ID do contato > ')
					if texto == 'V' or texto == 'v':
						chance = 5
						option = False
						msntempo(0.4,'Retornando tela inicial','CADASTRO DE CONTATOS')
					else:
						opcao = int(texto) 
						achou = len(procurarid(opcao))
						if achou == 1:
							print('-----| Dados do contato para atualizar  |-----')
							print('ID\tNome\t\t\t\tCódigo\t\tTipo de contato')
							print('-'*77)
							c = procurarid(opcao)
							for x in c:
								print("{:0>4}\t{:<30}\t{:0>4}\t\t{}".format(x[0], x[1], x[2], x[3]))
							print()
							print('-----| Dados do novo contato |-----')
							nome = input('Nome: ')
							codigo = input('Código: ')
							print('----------| Setor |----------')
							print('[1]: Cônjugue\t[2]: Namorado(a)')
							print('[3]: Amigo(a)\t[4]: Família') 
							print('[5]: Trabalho\t[6]: Conhecido(a)')
				
							editar = True

							while editar:
								opcao2 = int(input('Selecione uma opção > '))

								if opcao2 == 1:
									setor = 'Cônjugue'
									editar = False
									chance = 5
									option = False
								elif opcao2 == 2:
									setor = 'Namorado(a)'
									editar = False
									chance = 5
									option = False
								elif opcao2 == 3:
									setor = 'Amigo(a)'
									editar = False
									chance = 5
									option = False
								elif opcao2 == 4:
									setor = 'Família'
									editar = False
									chance = 5
									option = False
								elif opcao2 == 5:
									setor = 'Trabalho'
									editar = False
									chance = 5
									option = False
								elif opcao2 == 6:
									setor = 'Conhecido(a)'
									editar = False
									chance = 5
									option = False
								else:
									print('Opção inválida')

							editarid('nome',nome,'codigo',codigo,'setor',setor,opcao)
							campos = localizarnome(nome) 
							system('cls')
							print('#'*15,'| CADASTRO DE CONTATOS |',datahora(),'|','#'*15)
							print('#'*5,'Notificação: Seja Bem Vindo(a)! (:D). E fique à vontade.')
							print('ID\tNome\t\t\t\tCódigo\t\tTipo de contato')
							print('-'*77)
							print('---------------------| Contato Atualizado com sucesso |----------------------')
							print('-'*77)
							for x in campos:
								print("{:0>4}\t{:<30}\t{:0>4}\t\t{}".format(x[0], x[1], x[2], x[3]))
							print('-'*77)
							sleep(1)
							msntempo(0.4,'Retornando tela inicial','CADASTRO DE CONTATOS')
						else:
							chance = chance + 1
							print('ID inválido. tente novamente')
							sleep(1)
				editar = False
				option = False
			else:
				atualizarzero()
		
		elif opcao == 'R' or opcao == 'r':
			if len(selecionar()) > 0:
				chance = 1
				tentativa = 4
				while chance <= tentativa:
					system('cls')
					print('#'*15,'| CADASTRO DE CONTATOS |',datahora(),'|','#'*15)
					print('#'*5,'Notificação: Não sabe o ID do contato? Volte ao inicio e pesquise.')
					print('-----------------------| Remover contato existente |-------------------------')
					print('Tentativa {} de {}...\t [V]: Voltar ao inicio'.format(chance,tentativa).center(77))
					texto = input('Informe o ID do contato > ')
					if texto == 'V' or texto == 'v':
						chance = 5
						option = False
						msntempo(0.4,'Retornando tela inicial','CADASTRO DE CONTATOS')
					else:
						opcao = int(texto) 
						achou = len(procurarid(opcao))
						if achou == 1:
							print('-----| Dados do contato a remover |-----')
							print('ID\tNome\t\t\t\tCódigo\t\tTipo de contato')
							print('-'*77)
							c = procurarid(opcao)
							for x in c:
								print("{:0>4}\t{:<30}\t{:0>4}\t\t{}".format(x[0], x[1], x[2], x[3]))
							print()
							print('Deseja realmente remover este contato?')
							print('[S]: Sim\t[N]: Não')
							opcao2 = input('Selecione uma opção > ')
							
							remover = True
							while remover:
								if opcao2 == 'S' or opcao2 == 's':
									removerid(opcao)
									print('-'*77)
									print('----------------------| contato removido com sucesso |-----------------------')
									print('-'*77)
									sleep(1)
									msntempo(0.4,'Retornando tela inicial','CADASTRO DE CONTATOS')
									chance = 5
									remover = False
								elif opcao2 == 'N' or opcao2 == 'n':
									remover = False
								else:
									print('Opção inválida')
						else:
							chance = chance + 1
							print('ID inválido. tente novamente')
							sleep(1)
				editar = False
				option = False
			else:
				removerzero()
				
		elif opcao == 'L' or opcao == 'l':
			if len(selecionar()) > 0:
				system('cls')
				print('#'*15,'| CADASTRO DE CONTATOS |',datahora(),'|','#'*15)
				print('#'*5,'Notificação: Seja Bem Vindo(a)! (:D). E fique à vontade.')
				print('---------------------| Procurar um contato pelo nome  |-----------------------')
				print()
				texto = input('Informe o nome do contato > ')
				if (len(localizarnome(texto)) > 0):
					system('cls')
					print('#'*15,'| CADASTRO DE CONTATOS |',datahora(),'|','#'*15)
					print('#'*5,'Notificação: Seu contato foi encontrado? (:S)')
					print('-----------------| Há um total de',contar(),'Contatos registrados |------------------')
					print('ID\tNome\t\t\t\tCódigo\t\tTipo de produto')
					print('-'*77)
					campos = localizarnome(texto)
					for x in campos:
						print("{:0>4}\t{:<30}\t{:0>4}\t\t{}".format(x[0], x[1], x[2], x[3]))
					print('-'*77)
					print('------------------------| Contato(s) encontrado(s) |-------------------------')
					print('-'*77)
					sleep(1)
					input('\nTecle ENTER para retornar a tela principal.')
					sleep(1)
					msntempo(0.4,'Retornando tela inicial','CADASTRO DE CONTATOS')
					option = False
					
				else:
					system('cls')
					print('#'*15,'| CADASTRO DE CONTATOS |',datahora(),'|','#'*15)
					print('#'*5,'Notificação: Seu Contato foi encontrado? (:S)')
					print('-'*77)
					print('-------------------------| Contato não encontrado |--------------------------')
					print('-'*77)
					sleep(1)
					msntempo(0.4,'Retornando tela inicial','CADASTRO DE CONTATOS')
					option = False
		
		elif opcao == 'S' or opcao == 's':
			option = False
			menu = False

		else:
			print('Opção inválida')
			sleep(2)
			option = False

conexao.close()	
msntempo(0.1,'Desonectando o banco de dados.','CADASTRO DE CONTATOS')
msntempo(0.1,'Encerrando Programa.','CADASTRO DE CONTATOS')
print('#'*15,'| CADASTRO DE CONTATOS |',datahora(),'|','#'*15)
print('#'*5,'Notificação: Aguardamos sua volta! (:D).')
print('#'*28,'Programa Encerrado!','#'*28)

