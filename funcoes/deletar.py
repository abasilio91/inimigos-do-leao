import json
from atualizar import *
from criar import *
from ler import *
from constante_textos import *

def deleta_entrada():
  historico = get_historico()
  print(ENTRA_ID_HISTORICO)

  historico_filtrado = {}
  for chave, valor in historico.items():
      if valor['status'] == 'ativo':
        historico_filtrado[chave] = valor
  print(historico_filtrado)

  id = input(ENTRA_ID_PARA_ATUALIZAR)

  if id not in historico.keys():
    print(ERRO_CHAVE_NAO_EXISTE)

  elif historico[id]["status"] == 'deletado':
    print(ERRO_CHAVE_DELETADA)

  else:
    historico[id]["status"] = 'deletado'
    print(SAIDA_SUCESSO_DELETADO)
    atualiza_historico(historico)