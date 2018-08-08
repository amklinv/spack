##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-graphviz
#
# You can edit this file again by typing:
#
#     spack edit py-graphviz
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PyGraphviz(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/xflr6/graphviz/archive/0.8.1.tar.gz"

    version('0.8.4', sha256='53949a3662a2805f78a5479fa240af9f68374074b042b020bfcbc38ec3022b61')
    version('0.8.3', sha256='0ec404e5902759ec3631d2adfea7cfbfbffd9aa29a0356b7b68e685154b34399')
    version('0.8.2', sha256='bbe1b086b9b34db6037a83d5c8158de63a40d36c0415c7eea7c26df43252e3de')
    version('0.8.1', sha256='19fa90669493b86df0d4adb9ee55147de92329f143480218d1c4eb91fa877cfa')
    version('0.8',   sha256='f4e4c96a52848c531557b2fd6f45aa2e588ef8b32c40949bd876362f0bf2187f')
    version('0.7.1', sha256='ddf783e5e75a9621950f1492e253d8502c732c8bdffc7a30295a5d046e1d4056')
    version('0.7',   sha256='acb78332f4735610596c777fc5bbeea7e4e7c8537a2dadfe8fa1789972efc2c5')
    version('0.6',   sha256='edcf3e908f0d873e569af593166416affa6e87e08bedb8bddca5f50fc9799f2f')
    version('0.5.2', sha256='eb6eb17dbb154f428fd577aee33d4d52477f2f64a5b07cc26d2d308026efa4b8')
    version('0.5.1', sha256='00ace0aa15cda3ea61bd7882a7b3b9cedb2c026eed1f5b119a03722b906e693b')

    # FIXME: Add dependencies if required.
    depends_on('py-setuptools', type='build')
    # depends_on('py-foo',        type=('build', 'run'))

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
