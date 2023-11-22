import datetime

from functools import reduce
from atualizar import *
from constante_textos import *
from ler import *

def make_id():
  date = datetime.datetime.strftime(datetime.datetime.now(),"%Y,%m,%d,%H,%M,%S,%f")
  date = list(date.split(sep=","))

  digito_1 = reduce(lambda x,y: int(x)+int(y),date) % 10
  digito_2 = reduce(lambda x,y: int(x)**2+int(y)**2,date) % 10

  concat_value = digito_1*10 + digito_2
  id = date[:3]
  id.append(str(concat_value))
  id = ''.join(id)
  return id

def nova_receita():
  valor = float(input(ENTRA_ATUALIZACAO_VALOR))
  historico = get_historico()
  info = {
      make_id(): {
      "status": "ativo",
      "movimentacao": "receita",
      "valor": valor,
      "data": datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S.%f"),
      "dia": datetime.datetime.now().day,
      "mes": datetime.datetime.now().month,
      "ano": datetime.datetime.now().year
    }
  }
  historico.update(info)
  atualiza_historico(historico)
  print(SAIDA_SUCESSO_CRIA_RECEITAS.format(valor))

def nova_despesa():
  valor = float(input(ENTRA_ATUALIZACAO_VALOR))
  historico = get_historico()
  info = {
    make_id(): {
      "status": "ativo",
      "movimentacao": "despesa",
      "valor": (-1)*valor,
      "data": datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S.%f"),
      "dia": datetime.datetime.now().day,
      "mes": datetime.datetime.now().month,
      "ano": datetime.datetime.now().year
    }
  }

  historico.update(info)
  atualiza_historico(historico)
  print(SAIDA_SUCESSO_CRIA_DESPESAS.format(valor))

def novo_investimento():
  valor = float(input(ENTRA_ATUALIZACAO_VALOR))
  taxa = float(input(ENTRA_TAXA_INVESTIMENTO))
  historico = get_historico()
  info = {
    make_id(): {
      "status": "ativo",
      "movimentacao": "investimento",
      "valor": valor,
      "juros": taxa,
      "data": datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S.%f"),
      "dia": datetime.datetime.now().day,
      "mes": datetime.datetime.now().month,
      "ano": datetime.datetime.now().year
    }
  }

  historico.update(info)
  atualiza_historico(historico)
  print(SAIDA_SUCESSO_CRIA_INVESTIMENTOS.format(valor, taxa))

def novo_arquivo(title: str="historico"):
  try:
    open(f'inimigos_do_leao/arquivos/{title}.json','x')
    print(CRIA_ARQUIVOS)

  except:
    opcao = input(ERRO_CRIA_ARQUIVOS)
    if opcao.lower() == 'sim':
      content = ""
      with open("inimigos_do_leao/arquivos/historico.json", 'wt') as file:
        file.write(content)



