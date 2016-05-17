#!/usr/bin/env python
# Copyright 2016 ARC Centre of Excellence for Climate Systems Science
# author: Scott Wales <scott.wales@unimelb.edu.au>
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import print_function

from argparse import ArgumentParser, RawTextHelpFormatter
import inspect
import os
import re
import socket

# Matches Cylc sections - arbitrary text within multiple square brackets
#  '[[ example ]]' -> '[[', 'example'
section_re = re.compile('^\s*(\[+)\s*([^]]+)\s*\]+\s*$')

def make_portable(old, new, site):
    """
    Read the old suite.rc file, writing portable values to the new suite.rc
    file and non-portable values to the site.rc file
    """
    section = []
    dest = 'old'
    for line in old:
        section_match = section_re.match(line)
        if section_match:
            # Get the current section level from the number of brackets
            level = len(section_match.group(1))
            name = section_match.group(2)

            # Insert the section, then trim sections in case we've gone up a
            # level
            section.insert(level-1, name)
            section = section[0:level]

            # Both files get sections
            new.write(line)
            site.write(line)
        else:
            if len(section) > 2 and section[2] == 'directives':
                # Directives are always non-portable
                site.write(line)
            else:
                new.write(line)

    # Include the site file
    new.write('{% include "site/"+SITE+".rc" %}\n')

def main():
    """
    Make a Cylc suite more portable, by moving site-specific values to a config
    file within the 'site' directory.

    Creates a 'suite.rc.new' file within the suite directory with the new settings
    """
    parser = ArgumentParser(
            description=inspect.getdoc(main),
            formatter_class=RawTextHelpFormatter,
            )
    parser.add_argument('suite',
            help='Path to Cylc suite')
    parser.add_argument('--site',
            help='Site name to create')
    args = parser.parse_args()

    # Get the suite.rc file
    oldsuiterc_name = os.path.join(args.suite,'suite.rc')
    newsuiterc_name = os.path.join(args.suite,'suite.rc.new')

    # Get the site/$SITE.rc file
    site_path    = os.path.join(args.suite, 'site')
    siterc_name  = os.path.join(site_path, '%s.rc'%args.site)

    # Sanity checks
    if not os.path.isdir(site_path):
        os.mkdir(site_path) 
    if os.path.isfile(siterc_name):
        raise ValueError('Site file already exists: %s'%siterc_name)

    oldsuiterc = open(oldsuiterc_name,'r')
    newsuiterc = open(newsuiterc_name,'w')
    siterc     = open(siterc_name,'w')

    make_portable(oldsuiterc, newsuiterc, siterc)

    oldsuiterc.close()
    newsuiterc.close()
    siterc.close()

if __name__ == '__main__':
    main()
