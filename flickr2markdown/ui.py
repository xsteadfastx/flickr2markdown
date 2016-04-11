from configparser import ConfigParser
from os.path import expanduser, join
import click
import sys

from flickr2markdown.flickr import photos, markdown, single_photo


def get_api_key():
    config = ConfigParser()
    config.read(join(expanduser('~'), '.flickr2markdown'))

    api_key = config['API'].get('key')

    if not api_key:
        click.echo('Need the Flickr API key in ~/.flickr2markdown')
        sys.exit(1)

    return api_key


@click.command()
@click.version_option()
@click.option('--user', help='Flickr Username')
@click.option('--count', type=click.INT,
              help='Number of last pictures to fetch')
@click.option('--id', help='ID of a single image')
@click.option('--size',
              default='large',
              type=click.Choice(['small', 'medium', 'large']),
              help='Image size: small, medium, large')
def main(user, count, size, id):
    api_key = get_api_key()

    if count and count >= 1:
        pics = photos(user, api_key)[:count]

        for pic in pics:
            click.echo(markdown(pic, size))

    elif count == 0:
        sys.exit(0)

    elif id:
        click.echo(markdown(single_photo(id, api_key), size))
