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
#     spack install py-pyinstaller
#
# You can edit this file again by typing:
#
#     spack edit py-pyinstaller
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PyPyinstaller(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/pyinstaller/pyinstaller/releases/download/v3.3/PyInstaller-3.3.tar.gz"

    version('3.3.1',    sha256='715f81f24b1ef0e5fe3b3c71e7540551838e46e9de30882aa7c0a521147fd1ce')
    version('3.3',      sha256='b6c95cdbb45ac78a44723fa2992b58e14637cbefecafc22d3790af262a7fad6f')
    version('3.2.1',    sha256='9e688aa94b26fdf13205b9afda96ebdd7120435ad3ac385576962c5b87d9fc1d')
    version('3.2',      sha256='7598d4c9f5712ba78beb46a857a493b1b93a584ca59944b8e7b6be00bb89cabc')
    version('3.1.1',    sha256='b111d35d836237bf954e9b47dcb338da48a40210c318b2b0bc163dba8ca8e096')
    version('3.1',      sha256='5a28c3bb9d23ea644f9dc9e561e66471b83258d44063bcb108dfbbfe4af3c02b')
    version('3.0.dev8', sha256='72ae5e53633b545603d9622e9a3792bae41d6aef484a1ee146f093c2bbeddd47')
    version('3.0.dev7', sha256='d7e2f04a55eabd72ea7fdd5c48cb536b0fa52931cd870aa567635c3121ed9fc3')
    version('3.0.dev6', sha256='9539743bec52815b3758f6d8fb5d228baa767b24f2a28f261b8c0dca92caf67f')
    version('3.0',      sha256='8f9f9836ffebe71f9d9ced24001f8b27c0492574ed12a7a97c2c8810fb3fa210')

    # FIXME: Add dependencies if required.
    depends_on('py-setuptools', type='build')
    # depends_on('py-foo',        type=('build', 'run'))

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
