# flickr2markdown

Fetches last Flickr Uploads and convert them to markdown syntax for using it in a markdown blogging environment. For example with [pelican](http://getpelican.com).

```
Usage: flickr2markdown.py [OPTIONS]

Options:
  --user TEXT                  Flickr Username
  --count INTEGER              Number of last pictures to fetch
  --size [small|medium|large]  Image size: small, medium, large
  --help                       Show this message and exit.
```

## Installation
1. `virtualenv -p /usr/bin/python3 env`
2. `pip install -r requirements.txt`
