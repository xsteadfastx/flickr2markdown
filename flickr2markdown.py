from urllib.parse import urlencode
import click
import requests
import sys


API_KEY = '2207902126a225122e46533e82b6a947'


def source_url(farm, server, id, secret, size):
    '''url for direct jpg use'''
    if size == 'small':
        img_size = 'n'
    elif size == 'medium':
        img_size = 'c'
    elif size == 'large':
        img_size = 'b'

    return 'https://farm{}.staticflickr.com/{}/{}_{}_{}.jpg'.format(
        farm, server, id, secret, img_size)


def page_url(user_id, photo_id):
    '''flickr picture page url'''
    return 'https://www.flickr.com/photos/{}/{}/'.format(user_id, photo_id)


def markdown(photo_data, size):
    '''return markdown for one picture'''
    return '[![{}]({})]({})'.format(
        photo_data['title'],
        source_url(photo_data['farm'],
                   photo_data['server'],
                   photo_data['id'],
                   photo_data['secret'],
                   size),
        page_url(photo_data['owner'],
                 photo_data['id']))


def user_id(username):
    '''gets flickr user id from username'''
    query_string = urlencode({
        'method': 'flickr.people.findByUsername',
        'api_key': API_KEY,
        'username': username,
        'format': 'json',
        'nojsoncallback': '1'
    })

    r = requests.get('https://api.flickr.com/services/rest/?' + query_string)

    return r.json()['user']['id']


def photos(username):
    '''gets last uploaded pictures'''
    user = user_id(username)

    query_string = urlencode({
        'method': 'flickr.people.getPublicPhotos',
        'api_key': API_KEY,
        'user_id': user,
        'format': 'json',
        'nojsoncallback': '1'
    })

    r = requests.get('https://api.flickr.com/services/rest/?' + query_string)

    return r.json()['photos']['photo']


def single_photo(id):
    '''returns photo data for markdown method for a single picture'''
    query_string = urlencode({
        'method': 'flickr.photos.getInfo',
        'api_key': API_KEY,
        'photo_id': id,
        'format': 'json',
        'nojsoncallback': '1'
    })

    r = requests.get('https://api.flickr.com/services/rest/?' + query_string)
    data = r.json()['photo']

    photo_data = {
        'title': data['title']['_content'],
        'farm': data['farm'],
        'server': data['server'],
        'id': id,
        'secret': data['secret'],
        'owner': data['owner']['username']
    }

    return photo_data


@click.command()
@click.option('--user', help='Flickr Username')
@click.option('--count', type=click.INT,
              help='Number of last pictures to fetch')
@click.option('--id', help='ID of a single image')
@click.option('--size',
              default='large',
              type=click.Choice(['small', 'medium', 'large']),
              help='Image size: small, medium, large')
def print_links(user, count, size, id):
    if count and count >= 1:
        pics = photos(user)[:count]

        for pic in pics:
            print(markdown(pic, size))

    elif count == 0:
        sys.exit(0)

    elif id:
        print(markdown(single_photo(id), size))


if __name__ == '__main__':
    print_links()
