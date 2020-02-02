from PyMQL5 import PyMQL5


mql5 = PyMQL5()


def puts(symbol: str, start: int, limit: int) -> list:
    """Retorna todas as puts de um ativo."""
    ticker = symbol[0:4] + "o"
    res = []
    # Testa se existe o range de sufixos
    for n in range(start, limit):
        test = ticker + str(n)
        price = mql5.iClose(test, "Daily", 0)
        if bool(price):
            res.append(test)
    return res
