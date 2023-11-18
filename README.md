# inimigos-do-leao

Projeto de um gerenciador financeiro desenvolvido durante o curso da ADA - Vem Ser Tech. Projeto em construção.

## Desenvolvido por:
- [Adam Basilio](https://github.com/abasilio91)
- [Daniel]()
- [Gabriela]()
- [Lilian]()
- [Raphael]()

## Contextualização
Deverá ser desenvolvido um sistema para controle financeiro que receba as movimentações e as armazena em um arquivo csv ou json. O sistema deverá ser capaz de realizar as seguintes operações:
- Criar novos registros e identificar a data que o registro foi feito, qual tipo de movimentação, valor.
- Os tipos podem ser despesas, receita ou investimento:
  - No caso de receita, o valor deve ser tratado como numerico e armazenado normalmente.
  - No caso de despesas o valor deve ser recebido como positivo, mas armazenado como negativo
  - No caso de investimento, deve ter uma informação a mais de 'Montante', em que será calculado quanto o dinheiro rendeu desde o dia que foi investido. Para essa finalidade utilize a seguinte formula:  $M=C∗(1+i)t$ [Saiba Mais](https://matematicafinanceira.org/juros-compostos/).
    - considere tudo em dias.
- Ler registros: Deverá ser possível consultar os registros por data, tipo ou valor.
- Atualizar registros: No caso de atualização, pode-se atualizar o valor, o tipo e a data deverá ser a de atualização do registro.
- Deletar: Deverá ser possível deletar o registro (caso necessário, considere o indice do elemento como ID)

Requisitos:
- Crie uma função que atualize os valores de rendimento sempre que chamada
- Crie uma função exportar_relatorio, que seja possível exportar um relatorio final em csv ou json .
- Crie pelo menos uma função de agrupamento, que seja capaz de mostrar o total de valor baseado em alguma informação (mes, tipo...)
- Crie valores separados para identificar a data (dia, mes, ano)

## O sistema
O sistema consiste em um ChatBot em que o usuário informa qual ação deseja tomar entre criar, atualizar, deletar ou ler registros. Os registros são salvos em um arquivo no formato ```.json```. Os registros possíveis são: Receitas, Despesas e Investimentos. Nos dois primeiros casos, apenas o valor da movimentação é necessário. No último, deve ser informado também a taxa de rendimento, em dias.

## Exemplos
```
O que deseja fazer?
    1: Nova movimentação
    2: Atualizar movimentação
    3: Deletar movimentação
    4: Ver movimentações
    5: Gerar relatório
    0: Encerrar

    Opção:
>>> 1
Digite o tipo de movimentação:
  1 - Receita
  2 - Despesa
  3 - Investimento

  Opção:
>>> 1

Informe o valor: 1500
O que deseja fazer?
    1: Nova movimentação
    2: Atualizar movimentação
    3: Deletar movimentação
    4: Ver movimentações
    5: Gerar relatório
    0: Encerrar

    Opção:
>>> 0
>>> Operação encerrada pelo usuário.
```

## Próximas etapas
- [ ] Registrar de despesas e investimentos
- [ ] Ler, atualizar e deletar entradas
- [ ] Calcular valor previsto para investimentos
- [ ] Gerar relatório
- [ ] GUI
