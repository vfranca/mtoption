from mtoption import cli
from click.testing import CliRunner
from unittest import mock, skip
from .fixtures import series


runner = CliRunner()


@skip("retornando resultado inesperado")
@mock.patch("mtoption.option.mql5")
def test_exibe_as_puts_do_ativo(mql5):
    mql5.iClose.return_value = 0.19
    res = runner.invoke(cli.puts, ["bova11", 96, 99])
    assert res.output == "bovao96\nbovao98\n"
    assert res.exit_code == 0


def test_exibe_todas_as_series_do_tipo_de_opcao():
    res = runner.invoke(cli.option, ["series", "put"])
    expec = ""
    for month in series["put"]:
        expec += "%s %s\n" % (series["put"][month], month)
    assert res.output == expec
    assert res.exit_code == 0
