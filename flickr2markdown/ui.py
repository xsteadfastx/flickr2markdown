from configparser import ConfigParser
from os.path import expanduser, join
import click
import sys

from flickr2markdown.flickr import photos, markdown, single_photo, parse_url


def parse_config():
    config = ConfigParser()
    config.read(join(expanduser('~'), '.flickr2markdown'))

    return config


def get_api_key(config):
    api_key = config['API'].get('key')

    if not api_key:
        click.echo('Need the Flickr API key in ~/.flickr2markdown')
        sys.exit(1)

    return api_key


def get_defaults(config):
    return {
        'user': config['Defaults'].get('user', None),
        'size': config['Defaults'].get('size', None)

    }


@click.command()
@click.version_option()
@click.option('--user', help='Flickr Username')
@click.option('--count', type=click.INT,
              help='Number of last pictures to fetch')
@click.option('--id', help='ID of a single image')
@click.option('--url', help='URL of a single image')
@click.option('--size',
              default='large',
              type=click.Choice(['small', 'medium', 'large']),
              help='Image size: small, medium, large')
def main(user, count, size, id, url):
    config = parse_config()
    api_key = get_api_key(config)
    defaults = get_defaults(config)

    if defaults['user']:
        user = defaults['user']

    if defaults['size'] and defaults['size'] in ['small', 'medium', 'large']:
        size = defaults['size']

    if count and count >= 1:
        pics = photos(user, api_key)[:count]

        for pic in pics:
            click.echo(markdown(pic, size))

    elif count == 0:
        sys.exit(0)

    elif id:
        click.echo(markdown(single_photo(id, api_key), size))

    elif url:
        click.echo(markdown(single_photo(parse_url(url), api_key), size))
