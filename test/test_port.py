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

from StringIO import StringIO
from textwrap import dedent
from cylcutil.port import *

def check_port(old, expect_new, expect_site):
    # Buffers for testing
    old_stream = StringIO(dedent(old).lstrip())
    new_stream = StringIO()
    site_stream = StringIO()

    make_portable(old_stream, new_stream, site_stream)

    # Check outputs against expected values
    assert new_stream.getvalue() == dedent(expect_new).lstrip()
    assert site_stream.getvalue() == dedent(expect_site).lstrip()

    old_stream.close()
    new_stream.close()
    site_stream.close()

def test_section():
    line = '[abc]'
    section_match = section_re.match(line)
    assert section_match
    assert section_match.group(1) == '['
    assert section_match.group(2) == 'abc'

def test_directives():
    old = """
        [[fcm_make2_um]]
            inherit = None, XC40
            [[[environment]]]
                UM_INSTALL_DIR = /projects/um1
                ROSE_TASK_N_JOBS = 6
            [[[directives]]]
                -l walltime = 00:50:00
                -l ncpus = 6
                -q = shared
        """
    new = """
        [[fcm_make2_um]]
            inherit = None, XC40
            [[[environment]]]
                UM_INSTALL_DIR = /projects/um1
                ROSE_TASK_N_JOBS = 6
            [[[directives]]]
        """
    site = """
        [[fcm_make2_um]]
            [[[environment]]]
            [[[directives]]]
                -l walltime = 00:50:00
                -l ncpus = 6
                -q = shared
        """
    check_port(old, new, site)

