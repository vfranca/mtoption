import click
from options import options


@click.command()
@click.argument("symbol")
@click.argument("start", type=int)
@click.argument("limit", type=int)
def puts(symbol, start, limit):
    """Exibe as puts do ativo."""
    symbols = options.puts(symbol, start, limit)
    for s in symbols:
        click.echo(s)
    return 0
