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
#     spack install tensorflow
#
# You can edit this file again by typing:
#
#     spack edit tensorflow
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PyTensorflow(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/tensorflow/tensorflow/archive/v1.4.0.tar.gz"

    version('1.10.0-rc0', sha256='0f02347f4e3993a97f790a795d5257ee5d43e7671979cab2f12c285adf787009')
    version('1.9.0-rc2',  sha256='0ecfea51cf4e14c082d1d42d54cb23371d3d46e86549435c8f6c5ff694287a76')
    version('1.9.0-rc1',  sha256='fff9f72ae12f3e3b5cfa924a1d751147decea4172fd02760aa1a3f9b04d5616a')
    version('1.9.0-rc0',  sha256='73045c7145eea62b0389dc9b381bf854393f09cf39c8537e0934d54ec18b3e1c')
    version('1.9.0',      sha256='ffc3151b06823d57b4a408261ba8efe53601563dfe93af0866751d4f6ca5068c')
    version('1.8.0-rc1',  sha256='55aeedc49382a3781c4cfbae647e37a5ea7bd159e743f7d1fcd445f6b13b31ac')
    version('1.8.0-rc0',  sha256='f7614087f2c6eef0c24e4ae54adb9cc93fe0a0919c24ec25c58c8139c3da5e05')
    version('1.8.0',      sha256='47646952590fd213b747247e6870d89bb4a368a95ae3561513d6c76e44f92a75')
    version('1.7.1',      sha256='3147f8c60d1f30da23a831bcf732e74b935dcee7c62e4b8b85f0f093030b52c8')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

