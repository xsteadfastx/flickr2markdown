Fetches last Flickr uploads and convert them to markdown syntax for using it in a markdown blogging environment. For example with `pelican <http://getpelican.com>`_.::

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

The config is needed for the flickr API key. It needs to be located in ``~/.flickr2markdown``. You can obtain a flickr API key `here <https://www.flickr.com/services/apps/create/apply>`_.

Example::

        [API]
        key = abc123

        [Defaults]
        user = marvinxsteadfast
        size = large


Example
-------

Input::

        $ flickr2markdown --user marvinxsteadfast --count 5

Output::

        [![Rodin](https://farm2.staticflickr.com/1531/26272005452_7bd8175256_b.jpg)](https://www.flickr.com/photos/8810721@N07/26272005452/)
        [![Rodin](https://farm2.staticflickr.com/1548/25761633043_a703e1099a_b.jpg)](https://www.flickr.com/photos/8810721@N07/25761633043/)
        [![Paris](https://farm2.staticflickr.com/1485/26364375095_e6bff59174_b.jpg)](https://www.flickr.com/photos/8810721@N07/26364375095/)
        [![Paris](https://farm2.staticflickr.com/1645/26091495910_babf3f132a_b.jpg)](https://www.flickr.com/photos/8810721@N07/26091495910/)
        [![Paris](https://farm2.staticflickr.com/1560/25761607033_09174223dc_b.jpg)](https://www.flickr.com/photos/8810721@N07/25761607033/)

