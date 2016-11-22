'''
Created on Nov 21, 2016

    v1 = Vector([7.887, 4.138]);
    v2 = Vector([-8.802, 6.776]);
    
    print "Dot product 1:" + str(vdot(v1, v2));

@author: iaskarov
'''

from math import fsum, sqrt, pow, fabs, acos, pi, sin, tan, cos;
from types import NoneType;

class Vector(object):

    _magnitude = None;
    _direction = None;
    _zero = False;
    _unit = None;
    
    def __init__(self, coordinates):
        
        try:
            if not coordinates:
                raise ValueError();
            self.coordinates = tuple(coordinates);
            self.dimention = len(coordinates);
            self.dimention = len(coordinates);
            self.magnitude = tuple(coordinates);
            self.direction = tuple(coordinates);
            self.unit = self.magnitude;
        
        except ValueError as ve:
            raise ValueError("Coordinates must be non-empty");
        except TypeError as te:
            raise TypeError("Coordinates must be iterable");

    @property
    def zero(self):
        return self._zero;
    
    @zero.setter
    def zero(self, magnitude):
        if(magnitude == 0x0):
            self._zero = True;

    @property
    def unit(self):
        return self._unit;
    
    @unit.setter
    def unit(self, magnitude):
        if not self.zero:
            vaux = [];
            for vix in self.coordinates:
                vaux.append(1/self.magnitude * vix);
            self._unit = vaux;

    @property
    def magnitude(self):
        return self._magnitude;
    
    @magnitude.setter
    def magnitude(self, coordinates):
        
        aux = 0x0;
        
        for vix in coordinates:
            aux += pow(vix, 0x02);
        
        self._magnitude = fabs(sqrt(aux));
        self.zero = self.magnitude;

    @property
    def direction(self):
        return self._direction;
    
    @direction.setter
    def direction(self, coordinates):
        
        if not self.zero:
            vaux = [];
            for vix in coordinates:
                vaux.append((1/self.magnitude) * vix);
            self._direction = vaux;
    
    def __str__(self):
        return 'Vector: {} \nMagnitude: {} \nDirection: {} \n '.format(self.coordinates, self.magnitude, self.direction);
    
    def __eq__(self, v):
        return self.coordinates == v.coordinates;     
