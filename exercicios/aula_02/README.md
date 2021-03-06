# Exercícios - Aula 02


## Exercício 1:

Escreva um programa que receba o ano de nascimento e que retorne a geração à qual a pessoa pertence. Para definir a qual geração uma pessoa pertence temos a seguinte tabela:

|Geração|Intervalo|
|:-----:|:-------:|
|Baby Boomer|Até 1964
|Geração X|1965 - 1979
|Geração Y| 1980 - 1994
|Geração Z| 1995 - Atual

Para testar se seu script está funcionando, considere os seguintes resultados esperados:

- Ano de nascimento = 1988: Geração Y
- Ano de nascimento = 1958: Geração Baby Boomer
- Ano de nascimento = 1996: Geração Z

## Exercício 2:

Escreva um script em Python que represente uma quitanda. O seu programa deverá apresentar as opções de frutas e a cada vez que uma fruta for selecionada, a fruta deverá ser adicionada em uma cesta de compras.

Menu principal:

``` python
Quitanda:
1: Ver cesta
2: Adicionar frutas
3: Sair

Digite a opção desejada:
```

``` python
Menu de frutas:

Escolha fruta desejada:
1 - Banana
2 - Melancia
3 - Morango

Digite à opção desejada: 2
Melancia adicionada com sucesso!

```
Os menus 1 e 2 deverão retornar ao menu principal após executar suas respectivas tarefas.

Você deverá validar as opções digitadas pelo usuário (caso ele digite algo errado, a mensagem _Digite uma opção inválida_ deve ser exibida).

O programa deverá ser encerrado apenas se o usuário digitar a opção 3.

## Exercício 3:

Aproveitando o exercício anterior, incremente a sua quitanda para consolidar o cálculo do valor total de sua cesta de compras. Deverá ser adicionado ao seu menu inicial a opção _checkout_ e esta deverá listar os produtos de sua cesta bem como o valor total:


``` python
Menu:
1: Ver cesta
2: Adicionar Frutas
3: Checkout
4: Sair

Digite a opção desejada:
```

A saída do checkout deverá ser da seguinte maneira:

``` python
Total de compras: 15,00
Cesta de compras: Banana, Morango, Melancia
```

Considere os seguintes preços:

Banana: 3.50
Melancia: 7.50
Morango: 5.00

Dica: você pode armazenar os dados das frutas e seus respectivos preços em um dicionário.

Escreva um script em Python que receba dois números e que realize as seguintes operações:

- Soma de dois números
- Diferença de dois números

No exemplo foram digitados os números 4 e 2. O resultado deverá ser apresentado da seguinte forma:

```
------------------------------
Soma: 4 + 2 = 6
Diferença: 4 - 2 = 2
```

