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
#     spack install py-flask-cors
#
# You can edit this file again by typing:
#
#     spack edit py-flask-cors
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PyFlaskCors(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/corydolphin/flask-cors/archive/3.0.3.tar.gz"

    version('3.0.6', sha256='86938cad76f469d4dba43df994c90d23f6d8f57628f1ab3cfa65ff6e65a678cb')
    version('3.0.5', sha256='c959871aa1efa98abedc174ec832641acefc256457ac0ad082f63c0db696ceed')
    version('3.0.4', sha256='abaeadddaaab5fd0eeed85fc0bf574bc12a97adeb88959bda12f9ff8276504b8')
    version('3.0.3', sha256='bbd7c63ed38f9ef3f096582408429dd65150e106006a87ad9fb86e854dd95b8e')
    version('3.0.2', sha256='777bfecd00b5b18f1aadac5ec720be2d3d2022577180a7df26642e09f6d2e1ca')
    version('3.0.1', sha256='8de9f5f5ecb1bce74d00f6f063ce1081b663b96f2a3efce91c6d9c4aeabfd994')
    version('3.0.0', sha256='dd981515115d51dee44d7b830adf0a9de8ed9c04058c6143d483f570c8955cbc')
    version('2.1.3', sha256='230f1d60d6771fa646ba417bfefeeb09e40e21eea2419d18d9088935963256de')
    version('2.1.2', sha256='ae7cc8eb4c2637585baf9b233145a53a9628a6d752d44821ad4903f8324e069f')
    version('2.1.1', sha256='94759d8cf9aa65e5cbed5627236c2dcada1f4c1e645808cc9e0940af87a96e2b')

    # FIXME: Add dependencies if required.
    depends_on('py-setuptools', type='build')
    # depends_on('py-foo',        type=('build', 'run'))

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
