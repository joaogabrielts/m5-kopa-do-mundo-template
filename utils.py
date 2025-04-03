from datetime import datetime
from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError


def data_processing(data: dict):
    first_cup_year = int(data["first_cup"].split("-")[0])
    titles = data["titles"]

    # Verifica se o número de títulos é negativo
    if titles < 0:
        raise NegativeTitlesError()

    # Verifica se o ano da primeira copa é válido
    if first_cup_year < 1930 or (first_cup_year - 1930) % 4 != 0:
        raise InvalidYearCupError()

    # Calcula o número de copas disputadas desde a primeira participação
    current_year = datetime.now().year
    total_cups = len(range(first_cup_year, current_year + 1, 4))

    # Verifica se o número de títulos é possível
    if titles > total_cups:
        raise ImpossibleTitlesError()

    return "Dados validados com sucesso!"
