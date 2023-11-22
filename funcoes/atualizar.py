import json
from chat import *
from criar import *
from constante_textos import *
from ler import *

def atualiza_entrada():
    historico = get_historico()

    entra_id = input(ENTRA_ATUALIZACAO_ID_MOVIMENTACAO)
    if entra_id not in historico:
        print(ERRO_ID_NAO_ENCONTRADO)

    print(SAIDA_LER_MOVIMENTACAO, historico[entra_id])

    tipo_movimentacao = input(ENTRA_ATUALIZACAO_TIPO_MOVIMENTACAO)
    if tipo_movimentacao not in ("receita", "despesa", "investimento"):
        print(ERRO_MOVIMENTACAO_INVALIDA)

    novo_valor = input(ENTRA_ATUALIZACAO_VALOR)
    try:
        novo_valor = float(novo_valor)

        if tipo_movimentacao == "receita":
          if "juros" in historico[entra_id].keys():
            del historico[entra_id]["juros"]

        if tipo_movimentacao == "despesa":
          novo_valor *= -1
          if "juros" in historico[entra_id].keys():
            del historico[entra_id]["juros"]

        if tipo_movimentacao == "investimento":
          taxa = float(input(ENTRA_TAXA_INVESTIMENTO))
          historico[entra_id]['juros'] = taxa

        historico[entra_id]["movimentacao"] = tipo_movimentacao
        historico[entra_id]["valor"] = novo_valor

        atualiza_historico(historico)
        print(SAIDA_SUCESSO_MOVIMENTACAO)

    except ValueError:
       print(ERRO_MOVIMENTACAO_VALOR)
    
def atualiza_historico(historico):
    with open('../arquivos/historico.json','wt') as file:
       json.dump(historico, file, indent=4, sort_keys=True)