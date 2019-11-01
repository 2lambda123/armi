# Copyright 2019 TerraPower, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Inconel 800."""
from armi.materials.material import Material


class Inconel800(Material):
    name = "Inconel800"

    def setDefaultMassFracs(self):
        self.setMassFrac("NI", 0.325)
        self.setMassFrac("CR", 0.21)
        self.setMassFrac("FE", 0.457)
        self.setMassFrac("C", 0.0005)
        self.setMassFrac("AL27", 0.00375)
        self.setMassFrac("TI", 0.00375)

    def density(self, Tk=None, Tc=None):
        return 7.94
