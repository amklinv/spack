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
#     spack install py-opencv-python
#
# You can edit this file again by typing:
#
#     spack edit py-opencv-python
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PyOpencvPython(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/skvark/opencv-python/archive/12.tar.gz"

    version('17', sha256='72396ee24cddcd68860f82c769a6fa51c78e2082e1b5ffb372db6ee25109deb9')
    version('16', sha256='f438f7998532b4420678eb28a9c8aa6b62312968617287329949bcbc0d630012')
    version('15', sha256='63a742959f411ca976f67a3225db453b01fff563484190a158acb19a8eb231d4')
    version('14', sha256='66cc5d0ef48adece6909f2e9380f04347e02daa9e580aec66309a30132d0d457')
    version('13', sha256='d65bc14e9101ba89c6220bdd745ab7f436d0facbd07f6d5101a6bd3004223a5e')
    version('12', sha256='f836f68a7659b59137acf0e8bac5d96f1c939eb09e271648f5799c5f73cc996f')
    version('11', sha256='c9edc7a435b9d0cb114ae29103e3cdc69a5f571350a5b40a717924befdd4e999')
    version('10', sha256='a0ab0f9dabb7a41d2b3f19b951e5b49173a3e3295fa2e2c3fa4ff7de6b34cc40')
    version('9',  sha256='f00f2c9206bc88cacd8e42927c039e84c3e7fc646e998d326633a79f3e29d41f')
    version('8',  sha256='49ba4508fc46c91d48cfb243b623e79f8140a3e52d8fd70bce0b89caf380ce11')

    # FIXME: Add dependencies if required.
    #depends_on('py-setuptools', type='build')
    depends_on('py-pip', type=('build','run'))
    depends_on('opencv')

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
