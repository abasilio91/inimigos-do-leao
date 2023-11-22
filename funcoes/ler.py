import json
from atualizar import *
from calcular import *
from chat import *
from criar import *
from constante_textos import *
from deletar import *

def get_entrada():
    historico = get_historico()
    print(SAIDA_SUCESSO_TITULO_HISTORICO)
    for id, entrada in historico.items():
        print(SAIDA_SUCESSO_HISTORICO.format(id, entrada['data'], entrada['movimentacao'], entrada['valor']))

def get_relatorio():
  historico = get_historico()
  print(ENTRA_ID_HISTORICO)
  historico_filtrado = {}
  for chave, valor in historico.items():
      if valor['status'] == 'ativo':
        historico_filtrado[chave] = valor
  print(json.dumps(historico_filtrado, indent = 4))
  return historico_filtrado

def get_historico():
  with open('../arquivos/historico.json','r') as file:
    conteudo = file.read()
    if len(conteudo) == 0:
      historico = {}
    else:
      historico = json.loads(conteudo)
  return historico

def get_investimentos():
  historico = get_historico()
  historico_filtrado = {}
  for chave, valor in historico.items():
    if valor['status'] == 'ativo' and valor['movimentacao'] == 'investimento':
      historico_filtrado[chave] = valor
  return historico_filtrado