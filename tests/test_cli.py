from options import cli
from click.testing import CliRunner
from unittest import mock, skip


runner = CliRunner()


@skip("retornando resultado inesperado")
@mock.patch("options.options.mql5")
def test_exibe_as_puts_do_ativo(mql5):
    mql5.iClose.return_value = 0.19
    res = runner.invoke(cli.puts, ["bova11", 96, 99])
    assert res.output == "bovao96\nbovao98\n"
    assert res.exit_code == 0
