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

from .x16rChain import x16rChain

class Ravencoin(x16rChain):
    def __init__(chain, **kwargs):
        print("Init Ravencoin")
        chain.name = 'Ravencoin'
        chain.code3 = 'RVN'
        chain.address_version = '\x3c'
        chain.script_addr_vers = '\x7a'
        chain.magic = '\x52\x41\x56\x4e'
        x16rChain.__init__(chain, **kwargs)
    
    datadir_conf_file_name = 'Raven.conf'
    datadir_rpcport = 8766
    datadir_p2pport = 8767
