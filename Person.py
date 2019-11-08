#!/usr/bin/env python3

#
#  Person.py Define person class to poll.
#  Copyright (C) 2019 Carlos Nathan Peña Martinez
#                     carlos.nathan08@gmail.com
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.


class Person:
    
    def __init__(self,age=18,sex,income=1825, education=12, race,religion,marital_status,sexual_orientetion,childrens=0,security_perception = 10):
        self.age = age              # years
        self.sex = sex              # M,F,I
        self.incoming= income       # dlls per year
        self.education = education  # years
        self.race = race            # 
        self.religion = religion    #
        self.marital_status= marital_status
        self.sexual_orientetion= sexual_orientetion
        self.childrens= childrens
        self.security_perception= security_perception # 0 insecure -> 10 secure
