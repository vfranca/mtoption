from options import __version__
from options import options
from unittest import mock


def test_version():
    assert __version__ == "0.1.0"


@mock.patch("options.options.mql5")
def test_pega_todas_as_puts_de_um_ativo(mql5):
    mql5.iClose.return_value = 0.19
    assert options.puts("bova11", 96, 99) == ["bovao96", "bovao97", "bovao98"]


@mock.patch("options.options.mql5")
def test_pega_o_preco_da_opcao(mql5):
    mql5.iClose.return_value = 0.19
    assert options.price("bovao96") == 0.19
