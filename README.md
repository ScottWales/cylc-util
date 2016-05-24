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

This will create a new file `~/cylc-run/mysuite/site/NCI.rc`, which contains
all of the site-specific runtime information (submission method, directives and
host). A new `suite.rc` file will be created as `suite.rc.new`, which has the
site specific information removed. The new suite file will include the site
file named by the Jinja variable `SITE`, eg. `{% set SITE='NCI' %}` will
include `site/NCI.rc`.

To port the suite to a new site make a copy of an existing site file and change
task directives as appropriate.

#### Limitations

Currently Jinja macros within the main suite.rc file are ignored, and section
contents are copied until the next section name. This means a suite file like

```
{% for foo in ['bar','baz'] %}
    [[ {{ foo }} ]]
        [[[ directives ]]]
            -ncpus = 14
{% endfor %}

    [[ other ]]
        ...
```

everything from the `[[[ directives ]]]` to the `[[ other ]]` line are moved to
the site file, including the Jinja tag. Some manual cleanup will be required in
this case.
