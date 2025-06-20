'''
Tabela de Decisão para check_discount_eligibility(age, is_student):

Regra | Condição: Idade      | Condição: Estudante | Resultado (Desconto)
------|----------------------|---------------------|-----------------------
1     | age < 0              | N/A                 | ValueError: "Idade não pode ser negativa."
2     | age >= 60            | N/A                 | "15% de desconto"
3     | age < 18 (e age >=0) | N/A                 | "10% de desconto"
4     | 18 <= age < 60       | True                | "20% de desconto"
5     | 18 <= age < 60       | False               | "Sem desconto"

Nota: A regra para idade >= 60 tem prioridade sobre as demais.
      A verificação de idade < 0 ocorre antes das demais regras de desconto.
'''
def check_discount_eligibility(age: int, is_student: bool) -> str:
    """
    Verifica a elegibilidade para desconto com base na idade e status de estudante.

    Args:
        age: A idade da pessoa.
        is_student: True se a pessoa for estudante, False caso contrário.

    Returns:
        Uma string indicando a porcentagem de desconto ou "Sem desconto".

    Raises:
        ValueError: Se a idade for negativa.
    """
    if age < 0:
        raise ValueError("Idade não pode ser negativa.")

    if age >= 60:
        return "15% de desconto"
    elif age < 18:
        return "10% de desconto"
    elif is_student:  # Implícito: 18 <= age < 60
        return "20% de desconto"
    else:  # Implícito: 18 <= age < 60 and not is_student
        return "Sem desconto"

