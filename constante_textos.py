CRIA_ARQUIVOS = "Arquivo de histórico criado com sucesso.\n\n"

ENTRA_ATUALIZACAO_ID_MOVIMENTACAO = "Informe o ID da movimentação que deseja atualizar: "
ENTRA_ATUALIZACAO_TIPO_MOVIMENTACAO = "Informe o tipo da movimentação (receita, despesa, investimento): "
ENTRA_ATUALIZACAO_VALOR = "Informe o valor: "
ENTRA_TAXA_INVESTIMENTO = "Digite a taxa diária do investimento, em porcentagem: "
ENTRA_ID_HISTORICO = """Abaixo está o seu histórico de lançamentos.
Copie o id correspondente caso deseje atualizar/deletar algum registro (ex. 202312345):\n"""
ENTRA_ID_PARA_ATUALIZAR = "\nInforme o id do registro que deve ser DELETADO do histórico (os id's estão no seu histórico acima): "
ENTRA_TAXA_JUROS = "Informe a taxa diária de rendimento (em porcentagem): "
ENTRA_DATA_FUTURA = "\nInforme a data que deseja realizar o cálculo do montante (Exemplo: 20/01/2020): "

ERRO_ID_NAO_ENCONTRADO = "ID não encontrado."
ERRO_MOVIMENTACAO_INVALIDA = "Movimentação inválida"
ERRO_MOVIMENTACAO_VALOR = "Valor inválido."
ERRO_CHAVE_NAO_EXISTE = "\nA chave informada não consta do seu histórico.\n"
ERRO_CHAVE_DELETADA = "\nVocê já havia deletado esse registro.\n"
ERRO_OPCAO_INVALIDA = "Opção inválida.\n\n"
ERRO_CRIA_ARQUIVOS = "O arquivo de histórico já existe.\n Deseja sobrescrever o arquivo (sim ou não)?\n ATENÇÃO: Essa ação é IRREVERSÍVEL!\n"
ERRO_MOVIMENTACAO_INVALIDA = "Tipo de movimentação inválido."

SAIDA_LER_MOVIMENTACAO = "Informações atuais:"
SAIDA_SUCESSO_MOVIMENTACAO = "Movimentação atualizada com sucesso."
SAIDA_SUCESSO_DELETADO = "\nRegistro deletado com sucesso!\n"
SAIDA_SUCESSO_TITULO_HISTORICO = "Histórico Completo:"
SAIDA_RELATORIO_MOVIMENTACOES = "Segue abaixo o histórico de movimentações"
SAIDA_CRIAR_ARQUIVO_RELATORIO = "Relatório criado com sucesso!\n O Relatório se encontra na paste inimigos_do_leao/arquivos/relatorio.json\n"
SAIDA_TOTAL_RECEITAS = 'O seu total de receitas é R$ {:.2f}\n'
SAIDA_TOTAL_DESPESAS = 'O seu total de despesas é R$ {:.2f}\n'
SAIDA_TOTAL_INVESTIMENTOS = 'A soma dos valores investidos ao longo de {} dias é: R$ {:.2f}\n'
SAIDA_TOTAL_VALORES_FUTUROS = 'A soma dos valores futuros ao longo de {} dias é: R$ {:.2f}\n'
SAIDA_SUCESSO_CRIA_RECEITAS = 'A receita de R$ {:.2f} foi adicionado com sucesso!\n'
SAIDA_SUCESSO_CRIA_DESPESAS = 'A despesa de R$ {:.2f} foi adicionado com sucesso!\n'
SAIDA_SUCESSO_CRIA_INVESTIMENTOS = 'O investimento de R$ {:.2f} sob taxa de {}% foi adicionado com sucesso!\n'
SAIDA_SUCESSO_HISTORICO = "ID: {}, Data: {}, Tipo: {}, Valor: {:.2f}"
SAIDA_ENCERRA_PROGRAMA = "Programa encerrado pelo usuário\nConte comigo na luta contra o Leão!\n"

CHAT_PAGINA1 = """
    O que deseja fazer:
    1: Criar novo histórico
    2: Atualizar histórico existente
    3: Mostrar o histórico completo
    4: Gerar relatórios
    0: Encerrar

    Opção: """

CHAT_PAGINA2 = """
  O que deseja fazer?
    1: Nova movimentação
    2: Atualizar movimentação
    3: Deletar movimentação
    4: Gerar relatório
    5: Voltar ao menu anterior
    0: Encerrar

    Opção: """

CHAT_PAGINA3 = """Digite o tipo de movimentação:
  1: Receita
  2: Despesa
  3: Investimento
  4: Voltar ao menu anterior
  0: Encerrar

  Opção: """

CHAT_PAGINA4 = """Digite o tipo de movimentação:
  1: Criar relatório de movimentaçõces
  2: Soma das receitas
  3: Soma das despesas
  4: Soma dos investimentos
  5: Saldo futuro
  6: Voltar ao menu anterior
  0: Encerrar

  Opção: """