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
Extract values stored in an atrribute
-
Provided by Wasp 0.0.04
    Args:
        ATTR: Attributes list to search
        ID: Name of the attribute to extract
    Returns:
        VAL: Value stored in the requested attribute
"""

ghenv.Component.Name = "Wasp_Get Attribute by Name"
ghenv.Component.NickName = 'GetAttr'
ghenv.Component.Message = 'VER 0.0.04\nNOV_16_2017'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = "Wasp"
ghenv.Component.SubCategory = "0 | Wasp"
try: ghenv.Component.AdditionalHelpFromDocStrings = "2"
except: pass


if ATTR is None:
    msg = "No attribute provided"
    ghenv.Component.AddRuntimeMessage(gh.GH_RuntimeMessageLevel.Warning, msg)
else:
    VAL = []
    for attr in ATTR:
        if attr.name == ID:
            VAL = attr.values