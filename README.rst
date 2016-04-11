Fetches last Flickr Uploads and convert them to markdown syntax for using it in a markdown blogging environment. For example with `pelican <http://getpelican.com>`_.::

        Usage: flickr2markdown [OPTIONS]

        Options:
          --version                    Show the version and exit.
          --user TEXT                  Flickr Username
          --count INTEGER              Number of last pictures to fetch
          --id TEXT                    ID of a single image
          --size [small|medium|large]  Image size: small, medium, large
          --help                       Show this message and exit.


Installation
------------

``pip install flickr2markdown``


Config
------

The config is needed for the flickr API key. It needs to be located in ``~/.flickr2markdown``. You can obtain a flickr api key `here <https://www.flickr.com/services/apps/create/apply>`_.

Example::

        [API]
        key = abc123
