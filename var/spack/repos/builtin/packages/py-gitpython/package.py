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
#     spack install py-gitpython
#
# You can edit this file again by typing:
#
#     spack edit py-gitpython
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PyGitpython(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/gitpython-developers/GitPython/archive/2.1.7.tar.gz"

    version('2.1.11', sha256='a2f803859374c1a346e28387aa870e85ed93e692357a8704f5de37aeae814718')
    version('2.1.10', sha256='bbe276c18cd405603bb2893b87e195effadd6872afa6ab28f79e4c0b441b467a')
    version('2.1.9',  sha256='c82d9a53a58142e5920e7cc9274d1efc3ad224d07cd32da192e64ae6bac61bb4')
    version('2.1.8',  sha256='2491dbfcd0cfae480ad805d3fcee0868c76a7aa4922e66bf88e4dd22c65134fe')
    version('2.1.7',  sha256='6966c4d91c9e8c0d782446157c123d009297fb36addcf6b1f55e1ec258c26b11')
    version('2.1.6',  sha256='d275ba6c6fc71f614cdffa0befe6354f42a1982266654de1714c5f7222dbbdc3')
    version('2.1.5',  sha256='286a4803abd46e12b464f892dcd80127c193d58eb0b4b17c7d0d7699b5eeb2c0')
    version('2.1.4',  sha256='85a32c520538b83c3f7618f6652c8c7e3bfd50a5dc9e442513967e8c42644a5d')
    version('2.1.3',  sha256='e63c045c7fcc9e52cfd06fbd6703168201ef24bbe15d39ec5d2d2232b740a6f9')
    version('2.1.2',  sha256='85babfe3f629f6a0e801f6ef7c6615d56b61569c15d8363e7fbc1d0caf27c63d')

    # FIXME: Add dependencies if required.
    depends_on('py-setuptools', type='build')
    # depends_on('py-foo',        type=('build', 'run'))

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
