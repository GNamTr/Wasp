# Wasp: Discrete Design with Grasshopper plug-in (GPL) initiated by Andrea Rossi
# 
# This file is part of Wasp.
# 
# Copyright (c) 2017, Andrea Rossi <a.rossi.andrea@gmail.com>
# Wasp is free software; you can redistribute it and/or modify 
# it under the terms of the GNU General Public License as published 
# by the Free Software Foundation; either version 3 of the License, 
# or (at your option) any later version. 
# 
# Wasp is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Wasp; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0 <https://www.gnu.org/licenses/gpl.html>
#
# Significant parts of Wasp have been developed by Andrea Rossi
# as part of research on digital materials and discrete design at:
# DDU Digital Design Unit - Prof. Oliver Tessmann
# Technische Universitt Darmstadt


#########################################################################
##                            COMPONENT INFO                           ##
#########################################################################

"""
Extract information from a Connection.
-
Provided by Wasp 0.0.04
    Args:
        PART: Parts from which to generate aggregation rules
        SELF_P: OPTIONAL // Create rules between connections belonging to the same part (True by default)
        SELF_C: OPTIONAL // Create rules between connection with same id (True by default)
    Returns:
        R: Generated aggregation rules
"""

ghenv.Component.Name = "Wasp_Rules Generator"
ghenv.Component.NickName = 'RuleGen'
ghenv.Component.Message = 'VER 0.0.04\nNOV_14_2017'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = "Wasp"
ghenv.Component.SubCategory = "0 | Wasp"
try: ghenv.Component.AdditionalHelpFromDocStrings = "2"
except: pass

import scriptcontext as sc
import Grasshopper.Kernel as gh

def main(parts, self_part, self_connection):
    ## check if Wasp is setup
    if sc.sticky.has_key('WaspSetup'):
        
        check_data = True
        
        ##check inputs
        if len(parts) == 0 or parts is None:
            check_data = False
            msg = "No part provided"
            ghenv.Component.AddRuntimeMessage(gh.GH_RuntimeMessageLevel.Waring, msg)
        
        if self_part == None:
            self_part = True
        
        if self_connection == None:
            self_connection = True
        
        if check_data:
            rules = []
            
            for part in parts:
                for conn in part.connections:
                    for other_part in parts:
                        skip_part = False
                        if self_part == False:
                            if part.name == other_part.name:
                                skip_part = True
                            
                        if skip_part == False:
                            for other_conn in other_part.connections:
                                skip_conn = False
                                if self_connection == False:
                                    if conn.id == other_conn.id:
                                        skip_conn = True
                                
                                if skip_conn == False:
                                    if conn.type == other_conn.type:
                                        r = sc.sticky['Rule'](part.name, conn.id, other_part.name, other_conn.id)
                                        rules.append(r)
            
            return [rules]
        else:
            return -1
    
    else:
        ## throw warining
        msg = "You must run the SetupWasp component before starting to build!"
        ghenv.Component.AddRuntimeMessage(gh.GH_RuntimeMessageLevel.Warning, msg)
        return -1



result = main(PART, SELF_P, SELF_C)

if result != -1:
    R = result[0]


