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
#     spack install py-commonmark-py
#
# You can edit this file again by typing:
#
#     spack edit py-commonmark-py
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PyCommonmarkPy(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/rtfd/CommonMark-py/releases/download/0.7.4/CommonMark-0.7.4.tar.gz"

    version('0.7.4', sha256='24678b72094398df96312fb927e274ccaf5148f25e47aca9f7fc062693ae7577')
    version('0.7.3', sha256='5f20ebd91614c8d339d4cded314894feb5d9a54c3b52c1ff9883794557149ea8')
    version('0.7.2', sha256='3cf8971d85b5782563ef8a3cc9c9ec92f09f4e6b856e42b0cbf1931927218e1b')
    version('0.7.1', sha256='6343a672a5fbae777fba077563ec429f67efc8c66adb30a7d4827d22d1ea238f')
    version('0.7.0', sha256='cb5afb8c6a5579e236ee5f08754c22cac4172317b23f72168a229bc0ed49d227')
    version('0.6.4', sha256='0a881b7526ab4c841498f71cb591d499f79fcaedb692e78e334bb3921d27d171')

    # FIXME: Add dependencies if required.
    depends_on('py-setuptools', type='build')
    # depends_on('py-foo',        type=('build', 'run'))

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
