#!/usr/bin/env python

from pyquery import PyQuery as pq
import json
import datetime


URL = 'http://wbond.net/sublime_packages/community'

filename = 'package-statistics-%s.json' % str(datetime.datetime.now().date())


def extract(p):

    return {
        'name':        p('h2 a').text(),
        'description': p('p').text(),
        'url':         p('a').attr('href'),
        'date':        p('.last_modified').text(),
        'version':     p('.version').text(),
        'installs':    p('.installs').text().split(' ')[0],
        'oses':        [ pq(x).attr('title') for x in p('.oses .OS') ],
        'author':      p('.author').contents()[2].strip(),
        'homepage':    p('.homepage a').text(),
    }


def main():

    # Download
    d = pq(url=URL)

    # Process
    extracted = [ extract(pq(x)) for x in d('.package') ]

    # Save
    json.dump(extracted, file(filename, 'w'))


if __name__ == '__main__':
    main()
