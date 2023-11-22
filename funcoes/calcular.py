from atualizar import *
from chat import *
from criar import *
from ler import *
from constante_textos import *

def soma_receitas():
  historico = get_historico()
  historico_filtrado = {}
  for chave, valor in historico.items():
      if valor['status'] == 'ativo':
        historico_filtrado[chave] = valor
  soma_receitas = 0
  for chave, valor in historico_filtrado.items():
      if valor['movimentacao'] == 'receita':
          soma_receitas += valor['valor']
  return soma_receitas

def soma_despesas():
  historico = get_historico()
  historico_filtrado = {}
  for chave, valor in historico.items():
      if valor['status'] == 'ativo':
        historico_filtrado[chave] = valor
  soma_despesas = 0
  for chave, valor in historico_filtrado.items():
      if valor['movimentacao'] == 'despesa':
          soma_despesas += valor['valor']
  soma_despesas *= -1
  return soma_despesas

def calcular_dias(dia, mes, ano, dia_futuro, mes_futuro, ano_futuro):

  data_inicio = datetime.datetime(ano, mes, dia)
  data_fim = datetime.datetime(ano_futuro, mes_futuro, dia_futuro)
  tempo = (data_fim - data_inicio).days
  return tempo

def soma_investimentos():
  dia_futuro, mes_futuro, ano_futuro = map(lambda x: int(x), input(ENTRA_DATA_FUTURA).split(sep = "/"))
  historico_filtrado = get_investimentos()

  investimento = []
  for item in historico_filtrado.keys():
    tempo = calcular_dias(int(historico_filtrado[item]['dia']), int(historico_filtrado[item]['mes']), int(historico_filtrado[item]['ano']), dia_futuro, mes_futuro, ano_futuro)
    calcular = calcular_montante(float(historico_filtrado[item]['valor']), float(historico_filtrado[item]['juros']), tempo)
    investimento.append(calcular)
  return sum(investimento), tempo

def calcular_montante(valor, taxa, tempo):
  return valor * (1 + taxa/100) ** tempo

def valores_futuros():
  receitas = soma_receitas()
  despesa = soma_despesas()
  investimento, tempo = soma_investimentos()
  return (receitas + investimento - despesa), tempo