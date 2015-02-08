# Skeleton of a CLI

import click

import zoetrope


@click.command('zoetrope')
@click.argument('baseurl', type=str)
@click.option('--urliterator', '-ui', type=str, multiple=True)
def cli(baseurl, urliterator):
    zoetrope.createURLs(baseurl, urliterator)

