from PyMQL5 import PyMQL5
from mtoptions import series


mql5 = PyMQL5()


def puts(prefix: str, start: int, limit: int) -> list:
    """Retorna todas as puts de um ativo."""
    res = []
    # Testa se existe o range de sufixos
    for n in range(start, limit):
        test = prefix + str(n)
        if bool(mql5.iClose(test, "Daily", 0)):
            res.append(test)
    return res


def price(symbol: str) -> float:
    """Retorna o preço da opção."""
    return mql5.iClose(symbol, "Daily", 0)


def get_series(type: str) -> dict:
    """Retorna as series do tipo de opção."""
    return series.series[type]
