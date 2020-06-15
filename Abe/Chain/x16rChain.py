# Copyright(C) 2020 by Tron Black.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/agpl.html>.

from . import BaseChain

class x16rChain(BaseChain):
    """
    A blockchain that hashes block headers using the x16r algorithm.
    The current implementation requires the xcoin_hash module.
    """

    def block_header_hash(chain, header):
    	#TODO - TB20200609 - Switch to x16r algo, then x16rV2, then KAWPOW
        import x16r_hash
        #from binascii import unhexlify, hexlify
        import ravencoin.core
        print("header hash x16r: " + ravencoin.core.b2lx(x16r_hash.getPoWHash(header)))

        return x16r_hash.getPoWHash(header)[::-1]  #Reverse is a quirk of Ravencoin
