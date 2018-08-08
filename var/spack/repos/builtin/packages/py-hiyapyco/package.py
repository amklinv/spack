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
#     spack install py-hiyapyco
#
# You can edit this file again by typing:
#
#     spack edit py-hiyapyco
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PyHiyapyco(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/zerwes/hiyapyco/archive/release-0.4.11.tar.gz"

    version('0.4.11', sha256='fb1e6ec9a7f148f194037d40001e54cad04b6505ddc4ed71554e30afa670ef62')
    version('0.4.10', sha256='85947c8c4ea517234c4ae44616b5cdae93c2176bb536f54e2d57117314036bf7')
    version('0.4.9',  sha256='92d3b15ebc3ae42e7a97ecbf39ceb2c4ab8738b3ad0b78def93fad01759af691')
    version('0.4.8',  sha256='4acc3829a9301f70c7f6739605d80fb518e34c246e4b6b5d1efbeaea61eaf5b2')
    version('0.4.7',  sha256='b539ae4048ddb9c41474619c1f1d72f54fe9dd121414e34e4476475f61435550')
    version('0.4.6',  sha256='ae514d5f08e1c67841170fabbc054373db32ce8179e1ff417fe183b3c9dc63ff')
    version('0.4.5',  sha256='dd8491f737ec0ef1a2ecf73fff78f1323d1567e8094bb2e3d8485b8fdc469030')
    version('0.4.4',  sha256='d56ff640da7359a9b95c5c5befc8724edf9c3ad779aff293fdd45dbf80f335e7')
    version('0.4.3',  sha256='b69c3a40d8a514572d262cd1a4f7766f58f477441143d5675d17f9647300074c')
    version('0.4.2',  sha256='cd8bbd9c24c61d3165b93ec1b763a67602a04adb08bbb3dbe9fa142e080dc970')

    # FIXME: Add dependencies if required.
    depends_on('py-setuptools', type='build')
    # depends_on('py-foo',        type=('build', 'run'))

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
