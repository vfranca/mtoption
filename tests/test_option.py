from mtoption import option
from unittest import mock
from .fixtures import series


@mock.patch("mtoption.option.mql5")
def test_pega_todas_as_puts_de_um_ativo(mql5):
    mql5.iClose.return_value = 0.19
    assert option.puts("bovao", 96, 99) == ["bovao96", "bovao97", "bovao98"]


@mock.patch("mtoption.option.mql5")
def test_pega_o_premio_da_opcao(mql5):
    mql5.iClose.return_value = 0.19
    assert option.premio("bovao96") == 0.19


def test_obtem_series():
    assert option.get_series("put") == series["put"]
