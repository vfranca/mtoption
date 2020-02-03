import click
from mtoptions import options


@click.group()
def option():
    """Console de scripts para MTOptions."""
    pass


@click.command()
@click.argument("symbol")
@click.argument("start", type=int)
@click.argument("limit", type=int)
def puts(symbol, start, limit):
    """Exibe as puts do ativo."""
    symbols = options.puts(symbol, start, limit)
    for symbol in symbols:
        price = options.price(symbol)
        click.echo("%s %.2f" % (symbol, price))
    return 0


@click.command()
@click.argument("type")
def series(type):
    """Exibe as séries das opções call e put."""
    all_series = options.get_series(type)
    for month in all_series:
        click.echo("%s %s" % (all_series[month], month))
    return 0


option.add_command(puts)
option.add_command(series)
