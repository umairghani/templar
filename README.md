# Python Template Library

* Author: Umair Ghani

## Description:

Python Templating Library. Based on python-jinja templating

You can find JINJA documentation here: [JINJA TEMPLATING DOCUMENTATION] (http://jinja.pocoo.org/docs/dev/templates/)

## Dependencies:

Tested on:

* python2 (Not been tested with python3)
* python-jinja2
* python-setuptools
* python-boto (optional for AWS support)


NOTE: all default values come from the environment variables. Any other values (from the cli or s3) gets appended to the environment variable only when the script runs.

````

Usage: templar [options]

Options:
  -h, --help            show this help message and exit
  -e ENVIRONMENT, --environment=ENVIRONMENT
                        Specity environment (default will try to get it from
                        aws)
  -t TEMPLATE, --template=TEMPLATE
                        Location of your template file
  -s STRING, --string=STRING
                        Template string (make sure to wrap in quotes)
  -d DESTINATION, --destination=DESTINATION
                        Path of where to dump the rendered template
  -j JSONFILE, --json=JSONFILE
                        Path to the json file with all the variables/values
                        (default will try to get it from s3)
  -v VALUES, --values=VALUES
                        Values in json format e.g '{"key":"value"}' (default
                        will try to get it from s3)
  -b BUCKET, --bucket=BUCKET
                        provide a s3 bucket (default will get from
                        userdata/metadata)
  -k KEY, --key=KEY     provide a s3 bucket key (default will get from
                        userdata/metadata)
  --secret=SECRET       provide a aws secret key (default will get from
                        userdata/metadata)
  --access=ACCESS       provide a aws access key  (default will get from
                        userdata/metadata)
  --src=SOURCEDIR       Source Directory to find all tmpl


````


Example:

````

$ templar -s 'Hello {{ name }}' -v '{"name": "Umair"}'
Hello Umair

$ templar -s 'Hello {{ name }}' -v '{"name": "Umair"}' -d /tmp/test
$ cat /tmp/test
Hello Umair

$ templar -s 'Hello {{ name }}' -j /tmp/values.json
Hello Umair

$ cat /tmp/content.tmpl
Hello {{ name }}
$ cat /tmp/blah/test.tmpl
Hello {{ name }}

$ templar --src /tmp/ -j /tmp/values.json
$ cat /tmp/blah/test /tmp/content
Hello Umair Hello Umair

````
