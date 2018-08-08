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
#     spack install py-pynacl
#
# You can edit this file again by typing:
#
#     spack edit py-pynacl
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PyPynacl(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/pyca/pynacl/archive/1.1.2.tar.gz"

    version('1.2.1', sha256='00ac0c2bfaa087de634a73a4e348f535f69c386fabf762adb4841728b5fe88b1')
    version('1.2.0', sha256='d5d78493bd2f1a41d5967f43a9ee43f9d469dbe4608bdcf798146e3704722530')
    version('1.1.2', sha256='448897f0cfe3607dc23a871fa4405ef00926179df27ee8dfd0e46d42c60d8968')
    version('1.1.1', sha256='ef5677f6bd76db27b44f231b1c0dfe8556242a11c7f9c7c6b285959097b049b6')
    version('1.1.0', sha256='a88f21c3adbabc7ccc3b7bba6f96fa96a904d7f04f233161df4f36e1bbc45d94')
    version('1.0.1', sha256='033fb4db0598773b34863b0bebf0e64985712aec449513e78bfe2afc410cd759')
    version('1.0',   sha256='38ee92da59fb3c41bd45c5f4d7eba424fcae830fa63c837de63ba9c12ab27edf')

    # FIXME: Add dependencies if required.
    depends_on('py-setuptools', type='build')
    # depends_on('py-foo',        type=('build', 'run'))

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
