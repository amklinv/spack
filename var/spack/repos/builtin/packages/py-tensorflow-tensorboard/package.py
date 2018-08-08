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
#     spack install tensorboard
#
# You can edit this file again by typing:
#
#     spack edit tensorboard
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PyTensorflowTensorboard(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/tensorflow/tensorboard/archive/0.4.0-rc3.tar.gz"

    version('1.10.0',    sha256='d003ee154e8ae85b0f8a34fd7f8bb82a7f0acface8ca80db982b3595e401794f')
    version('1.9.0',     sha256='95663d6c3d05243913ce433fa1cc86c64181f46e74b1fd9429e1b9e39ec5e59c')
    version('1.8.0',     sha256='9483087bafa68420c846c6fc0be8688c4922f1fc2fa4c1add9c278cf014c9846')
    version('1.7.0',     sha256='b56a61433d58eea51d1d08194521126d78b1d6a92a03a243f89108d3890758fa')
    version('1.6.0-rc0', sha256='dc8f21faf7f15f601995e2d48f39885b03312063ea37b833f19b853ec5729c04')
    version('1.6.0',     sha256='087242325ef3b91f1909e3fd3a873ad15e3c7703990ad8caab64736d9009bf62')
    version('1.5.1',     sha256='1b7e1a4f8ebfcc7037be0fe8da83e351e348fbe9f046b764e2c85a7e524fd252')
    version('1.5.0',     sha256='30d6e06ff5050a75dde394635334de83fb56587421ed61999fea2f919f00eff6')
    version('0.4.0-rc3', sha256='46cde304d6fc342977f43aa306c3bf388b27eaba6cadceb932eefa2b2e734d29')
    version('0.4.0',     sha256='45e87ab64754e29b66e5e1dcaff14ed924775643b0fa8f459edccb2acdf6bf38')

    # FIXME: Add additional dependencies if required.

