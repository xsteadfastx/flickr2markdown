from urllib.parse import urlencode
import requests
import re


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


def user_id(username, api_key):
    '''gets flickr user id from username'''
    query_string = urlencode({
        'method': 'flickr.people.findByUsername',
        'api_key': api_key,
        'username': username,
        'format': 'json',
        'nojsoncallback': '1'
    })

    r = requests.get('https://api.flickr.com/services/rest/?' + query_string)

    return r.json()['user']['id']


def photos(username, api_key):
    '''gets last uploaded pictures'''
    user = user_id(username, api_key)

    query_string = urlencode({
        'method': 'flickr.people.getPublicPhotos',
        'api_key': api_key,
        'user_id': user,
        'format': 'json',
        'nojsoncallback': '1'
    })

    r = requests.get('https://api.flickr.com/services/rest/?' + query_string)

    return r.json()['photos']['photo']


def single_photo(id, api_key):
    '''returns photo data for markdown method for a single picture'''
    query_string = urlencode({
        'method': 'flickr.photos.getInfo',
        'api_key': api_key,
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


def parse_url(url):
    '''parses url for photo id'''
    id_re = re.compile(r'https://www\.flickr\.com/photos/.+/(\d+)/.+')

    return id_re.search(url).group(1)
