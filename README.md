# Análise e Teste de Software: Exemplos Práticos

Este repositório contém exemplos práticos relacionados à análise e teste de software, abordando:
1.  Criação de uma função simples, seu fluxo de decisão e testes unitários com 100% de cobertura.
2.  Uso de uma tabela de decisão para guiar a criação de testes para uma função com múltiplas condições.

## Estrutura do Projeto

*   `grade_calculator.py`: Contém a função `calculate_average_grade` que calcula a média de uma lista de notas, validando as entradas.
*   `test_grade_calculator.py`: Testes unitários para `calculate_average_grade`, utilizando o módulo `unittest`.
*   `decision_example.py`: Contém a função `check_discount_eligibility` que determina um desconto com base na idade e status de estudante. Inclui uma tabela de decisão em seus comentários.
*   `test_decision_example.py`: Testes unitários para `check_discount_eligibility`, baseados na tabela de decisão.

## Questões Abordadas

### Questão 1: Função Simples, Fluxo de Decisão e Testes de Cobertura

A função `calculate_average_grade(grades: list) -> float` em `grade_calculator.py` serve como exemplo.
Seu fluxo de decisão envolve:
1.  Verificar se a lista de notas está vazia (levanta `ValueError`).
2.  Verificar se todas as notas são numéricas (levanta `TypeError`).
3.  Verificar se todas as notas estão no intervalo [0, 10] (levanta `ValueError`).
4.  Calcular a média se todas as validações passarem.

Os testes em `test_grade_calculator.py` são projetados para cobrir todos esses cenários e garantir 100% de cobertura das ramificações da função.

### Questão 2: Código com If/Else, Tabela de Decisão e Casos de Teste

A função `check_discount_eligibility(age: int, is_student: bool) -> str` em `decision_example.py` demonstra o uso de uma tabela de decisão.
A tabela de decisão (incluída nos comentários do arquivo `decision_example.py`) é a seguinte:

| Regra | Condição: Idade      | Condição: Estudante | Resultado (Desconto)                     |
|-------|----------------------|---------------------|------------------------------------------|
| 1     | age < 0              | N/A                 | `ValueError`: "Idade não pode ser negativa." |
| 2     | age >= 60            | N/A                 | "15% de desconto"                        |
| 3     | age < 18 (e age >=0) | N/A                 | "10% de desconto"                        |
| 4     | 18 <= age < 60       | True                | "20% de desconto"                        |
| 5     | 18 <= age < 60       | False               | "Sem desconto"                           |

Os testes em `test_decision_example.py` são derivados diretamente desta tabela para assegurar que cada regra lógica seja verificada.

## Como Executar os Testes

Os testes são escritos usando o módulo `unittest` do Python. Para executá-los, navegue até o diretório raiz do projeto e execute os seguintes comandos no seu terminal:

```bash
python -m unittest test_grade_calculator.py
python -m unittest test_decision_example.py
```

Alternativamente, para descobrir e rodar todos os testes automaticamente (assumindo que os arquivos de teste sigam o padrão `test_*.py`):

```bash
python -m unittest discover
```