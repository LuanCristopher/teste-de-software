def calculate_average_grade(grades: list) -> float:
    """
    Calcula a média das notas em uma lista.

    Args:
        grades: Uma lista de números representando as notas.

    Returns:
        A média das notas.

    Raises:
        ValueError: Se a lista de notas estiver vazia ou se alguma nota
                    estiver fora do intervalo de 0 a 10.
        TypeError: Se alguma nota não for um número.
    """
    if not grades:
        raise ValueError("A lista de notas não pode estar vazia.")

    total = 0
    count = 0

    for grade in grades:
        if not isinstance(grade, (int, float)):
            raise TypeError("Todas as notas devem ser números.")
        if not 0 <= grade <= 10:
            raise ValueError("As notas devem estar entre 0 e 10.")
        total += grade
        count += 1

    return total / count
