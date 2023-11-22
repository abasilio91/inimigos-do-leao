# inimigos-do-leao

Projeto de um gerenciador financeiro desenvolvido durante o curso da ADA - Vem Ser Tech.

## Desenvolvido por:
- [Adam Basilio](https://github.com/abasilio91)
- [Daniel Rodrigues](https://www.linkedin.com/in/danielrodrigues-ds/)
- [Gabriela Rodruigues](https://www.linkedin.com/in/gabrielarodriguesdados/)
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

<details> 
  <summary> Criar um registro de Receita </summary> 

```
    O que deseja fazer:
    1: Criar novo histórico
    2: Atualizar histórico existente
    3: Mostrar o histórico completo
    4: Gerar relatórios
    0: Encerrar

    Opção: 2

  O que deseja fazer?
    1: Nova movimentação
    2: Atualizar movimentação
    3: Deletar movimentação
    4: Gerar relatório
    5: Voltar ao menu anterior
    0: Encerrar

    Opção: 1
Digite o tipo de movimentação:
  1: Receita
  2: Despesa
  3: Investimento
  4: Voltar ao menu anterior
  0: Encerrar

  Opção: 1
Informe o valor: 1000
A receita de R$ 1000.00 foi adicionado com sucesso!

Digite o tipo de movimentação:
  1: Receita
  2: Despesa
  3: Investimento
  4: Voltar ao menu anterior
  0: Encerrar

  Opção: 0
Programa encerrado pelo usuário
Conte comigo na luta contra o Leão!
```
</details>

<details>

  <summary>Criar um registro de despesa </summary>

```
    O que deseja fazer:
    1: Criar novo histórico
    2: Atualizar histórico existente
    3: Mostrar o histórico completo
    4: Gerar relatórios
    0: Encerrar

    Opção: 2

  O que deseja fazer?
    1: Nova movimentação
    2: Atualizar movimentação
    3: Deletar movimentação
    4: Gerar relatório
    5: Voltar ao menu anterior
    0: Encerrar

    Opção: 1
Digite o tipo de movimentação:
  1: Receita
  2: Despesa
  3: Investimento
  4: Voltar ao menu anterior
  0: Encerrar

  Opção: 2
Informe o valor: 300
A despesa de R$ 300.00 foi adicionado com sucesso!

Digite o tipo de movimentação:
  1: Receita
  2: Despesa
  3: Investimento
  4: Voltar ao menu anterior
  0: Encerrar

  Opção: 0
Programa encerrado pelo usuário
Conte comigo na luta contra o Leão!
```

</details>

<details>

<summary>Ler os registros ativos</summary>

```
    O que deseja fazer:
    1: Criar novo histórico
    2: Atualizar histórico existente
    3: Mostrar o histórico completo
    4: Gerar relatórios
    0: Encerrar

    Opção: 3
Histórico Completo:
ID: 202311222, Data: 2023-11-22 18:02:50.269914, Tipo: despesa, Valor: -300.00
ID: 2023112220, Data: 2023-11-22 18:01:25.592452, Tipo: receita, Valor: 1000.00

    O que deseja fazer:
    1: Criar novo histórico
    2: Atualizar histórico existente
    3: Mostrar o histórico completo
    4: Gerar relatórios
    0: Encerrar

    Opção: 0
Programa encerrado pelo usuário
Conte comigo na luta contra o Leão!
```
</details>

<details>

<summary> Atualizar um registro </summary>

```
    O que deseja fazer:
    1: Criar novo histórico
    2: Atualizar histórico existente
    3: Mostrar o histórico completo
    4: Gerar relatórios
    0: Encerrar

    Opção: 3
Histórico Completo:
ID: 202311222, Data: 2023-11-22 18:02:50.269914, Tipo: despesa, Valor: -300.00
ID: 2023112220, Data: 2023-11-22 18:01:25.592452, Tipo: receita, Valor: 1000.00

    O que deseja fazer:
    1: Criar novo histórico
    2: Atualizar histórico existente
    3: Mostrar o histórico completo
    4: Gerar relatórios
    0: Encerrar

    Opção: 2

  O que deseja fazer?
    1: Nova movimentação
    2: Atualizar movimentação
    3: Deletar movimentação
    4: Gerar relatório
    5: Voltar ao menu anterior
    0: Encerrar

    Opção: 2
Informe o ID da movimentação que deseja atualizar: 2023112220
Informações atuais:
Informe o tipo da movimentação (receita, despesa, investimento): investimento
Informe o valor: 700
Digite a taxa diária do investimento, em porcentagem: 1.2
Movimentação atualizada com sucesso.

  O que deseja fazer?
    1: Nova movimentação
    2: Atualizar movimentação
    3: Deletar movimentação
    4: Gerar relatório
    5: Voltar ao menu anterior
    0: Encerrar

    Opção: 0
Programa encerrado pelo usuário
Conte comigo na luta contra o Leão!
```
</details>

<details>
  <summary>Criando um Relatório json</summary>

``` 
    O que deseja fazer:
    1: Criar novo histórico
    2: Atualizar histórico existente
    3: Mostrar o histórico completo
    4: Gerar relatórios
    0: Encerrar

    Opção: 4
Digite o tipo de movimentação:
  1: Criar relatório de movimentaçõces
  2: Soma das receitas
  3: Soma das despesas
  4: Soma dos investimentos
  5: Saldo futuro
  6: Voltar ao menu anterior
  0: Encerrar

  Opção: 1
Relatório criado com sucesso!
 O Relatório se encontra na paste inimigos_do_leao/arquivos/relatorio.json

Digite o tipo de movimentação:
  1: Criar relatório de movimentaçõces
  2: Soma das receitas
  3: Soma das despesas
  4: Soma dos investimentos
  5: Saldo futuro
  6: Voltar ao menu anterior
  0: Encerrar

  Opção: 0
Programa encerrado pelo usuário
Conte comigo na luta contra o Leão!
```

</details>

<details>
  <summary> Checando totais </summary>

``` 
    O que deseja fazer:
    1: Criar novo histórico
    2: Atualizar histórico existente
    3: Mostrar o histórico completo
    4: Gerar relatórios
    0: Encerrar

    Opção: 4
Digite o tipo de movimentação:
  1: Criar relatório de movimentaçõces
  2: Soma das receitas
  3: Soma das despesas
  4: Soma dos investimentos
  5: Saldo futuro
  6: Voltar ao menu anterior
  0: Encerrar

  Opção: 2
O seu total de receitas é R$ 0.00

Digite o tipo de movimentação:
  1: Criar relatório de movimentaçõces
  2: Soma das receitas
  3: Soma das despesas
  4: Soma dos investimentos
  5: Saldo futuro
  6: Voltar ao menu anterior
  0: Encerrar

  Opção: 3
O seu total de despesas é R$ 300.00

Digite o tipo de movimentação:
  1: Criar relatório de movimentaçõces
  2: Soma das receitas
  3: Soma das despesas
  4: Soma dos investimentos
  5: Saldo futuro
  6: Voltar ao menu anterior
  0: Encerrar

  Opção: 4

Informe a data que deseja realizar o cálculo do montante (Exemplo: 20/01/2020): 20/11/2024
A soma dos valores investidos ao longo de 364 dias é: R$ 53802.76

Digite o tipo de movimentação:
  1: Criar relatório de movimentaçõces
  2: Soma das receitas
  3: Soma das despesas
  4: Soma dos investimentos
  5: Saldo futuro
  6: Voltar ao menu anterior
  0: Encerrar

  Opção: 5

Informe a data que deseja realizar o cálculo do montante (Exemplo: 20/01/2020): 20/11/2024
A soma dos valores futuros ao longo de 364 dias é: R$ 53502.76

Digite o tipo de movimentação:
  1: Criar relatório de movimentaçõces
  2: Soma das receitas
  3: Soma das despesas
  4: Soma dos investimentos
  5: Saldo futuro
  6: Voltar ao menu anterior
  0: Encerrar

  Opção: 0
Programa encerrado pelo usuário
Conte comigo na luta contra o Leão!
```
</details>
