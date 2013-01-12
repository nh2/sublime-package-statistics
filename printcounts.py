#!/usr/bin/env python2

import sys
import json

# TODO argparse
package = sys.argv[1].lower()
countsfile = sys.argv[2]

counts = json.load(file(countsfile))

package_count = counts[package]

for date in sorted(package_count.iterkeys()):
    print date, package_count[date]
