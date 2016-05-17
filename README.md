# cylcutil

[![Documentation Status](https://readthedocs.org/projects/cylc-util/badge/?version=latest)](https://readthedocs.org/projects/cylc-util/?badge=latest)
[![Build Status](https://travis-ci.org/ScottWales/cylc-util.svg?branch=master)](https://travis-ci.org/ScottWales/cylc-util)
[![codecov.io](http://codecov.io/github/ScottWales/cylc-util/coverage.svg?branch=master)](http://codecov.io/github/ScottWales/cylc-util?branch=master)
[![Code Health](https://landscape.io/github/ScottWales/cylc-util/master/landscape.svg?style=flat)](https://landscape.io/github/ScottWales/cylc-util/master)
[![Code Climate](https://codeclimate.com/github/ScottWales/cylc-util/badges/gpa.svg)](https://codeclimate.com/github/ScottWales/cylc-util)
[![PyPI version](https://badge.fury.io/py/cylc-util.svg)](https://pypi.python.org/pypi/cylc-util)

Build Instructions:
-------------------

    pip install --user git+https://github.com/ScottWales/cylc-util
    # Ensure ~/.local/bin is on your PATH

Available Tools
---------------

### cylc-port

Make a suite more portable, by moving site specific details to the 'site' directory

    cylc-port --site NCI ~/cylc-run/mysuite
