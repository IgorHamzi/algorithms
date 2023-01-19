# :information_source: Algorithms 👩🏽‍💻 

Para fixar os conteúdos de algoritmos, o principal objetivo desse projeto é a resolução de problemas e otimização algoritmos. Muitos dos problemas apresentados são similares aos que aparecem em entrevistas de processos seletivos do tipo whiteboard, conhecidos por ocorrerem no processo de contratação de grandes companhias (Google, Amazon, Facebook, etc).


## :rocket: Stack utilizada

* **language:** Python



## :link: Habilidades desenvolvidas

* Utilizar diferentes estruturas de dados
* Treinar análise de complexidade de algoritimos
* Praticar interpretação de problemas;
* Resolver problemas de forma otimizada;
* Analisar corretamente a ordem de complexidade de um algoritmo.
* Praticar funções recursivas
* Praticar algoritmos de ordenação e algoritmos de busca

--- 

# Requisitos do projeto

## Obrigatórios

- [x] 1 - Número de estudantes estudando no mesmo horário (Algoritmo de busca)

```md
# Nos arrays temos 6 estudantes

# estudante             1       2       3       4       5       6
permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

target_time = 5  # saída: 3, pois a quarta, a quinta e a sexta pessoa estudante ainda estavam estudando nesse horário.
target_time = 4  # saída: 3, pois a quinta e a sexta pessoa estudante começaram a estudar nesse horário e a quarta ainda estava estudando.
target_time = 3  # saída: 2, pois a terceira e a quarta pessoa estudante ainda estavam estudando nesse horário.
target_time = 2  # saída: 4, pois a primeira, a segunda, a terceira e a quarta pessoa estudante estavam estudando nesse horário.
target_time = 1  # saída: 2, pois a segunda e a quarta pessoa estudante estavam estudando nesse horário.

Para esse exemplo, depois de rodar a função para todos esses `target_times`, julgamos que o melhor horário é o `2`, pois esse retornou `4`, já que 4 estudantes estavam presentes nesse horário!
```
- [x] 2 - Palíndromos (Recursividade)

```md
word = "ANA"
# saída: True

word = "SOCOS"
# saída: True

word = "REVIVER"
# saída: True

word = "COXINHA"
# saída: False

word = "AGUA"
# saída: False
```

- [x] 3 - Anagramas (Algoritmo de ordenação)

```md
first_string = "amor"
second_string = "roma"
# saída: True


first_string = "pedra"
second_string = "perda"
# saída: True


first_string = "pato"
second_string = "tapo"
# saída: True


first_string = "Amor"
second_string = "Roma"
# saída: True


first_string = "coxinha"
second_string = "empada"
# saída: False
```

## Bônus

- [x] 4 - Encontrando números repetidos (Algoritmo de busca)

```md
nums = [1, 3, 4, 2, 2]
# saída: 2

nums = [3, 1, 3, 4, 2]
# saída: 3

nums = [1, 1]
# saída: 1

nums = [1, 1, 2]
# saída: 1

nums = [3, 1, 2, 4, 6, 5, 7, 7, 7, 8]
# saída: 7
```

- [x] 5 - Palíndromos (Iteratividade)

---

### Projeto realizado no módulo de Ciência da computação do Curso de Desenvolvimento WEB da TRYBE.