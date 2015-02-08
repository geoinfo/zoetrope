# Skeleton of a CLI

import click

import zoetrope


@click.command('zoetrope')
@click.argument('count', type=int, metavar='N')
def cli(count):
    """Echo a value `N` number of times"""
    for i in range(count):
        click.echo(zoetrope.has_legs)
