import click
from mtoptions import options


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
