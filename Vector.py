'''
Created on Nov 21, 2016

    v1 = Vector([7.887, 4.138]);
    v2 = Vector([-8.802, 6.776]);
    
    print "Dot product 1:" + str(vdot(v1, v2));

@author: iaskarov
'''

from math import fsum, sqrt, pow, fabs, acos, pi;
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

def vadd(vector1, vector2):
    
    vaux = [];
    for v1, v2 in zip(vector1.coordinates, vector2.coordinates):
        vaux.append(v1 + v2);
    return Vector(vaux);
    
def vsubtract(vector1, vector2):
    
    vaux = [];
    for v1, v2 in zip(vector1.coordinates, vector2.coordinates):
        vaux.append(v1 - v2);
    return Vector(vaux);

def vcomponent(vector1, vector2):
    return vsubtract(vector1, vector2);

def vdot(vector1, vector2):
    
    dot = 0x0;
    for v1, v2 in zip(vector1, vector2):
        dot += round(float(v1) * float(v2), 3);
    return dot;

def vangle(vector1, vector2, rad=False):
    
    rads = acos(vdot(vector1.coordinates, vector2.coordinates)/(vector1.magnitude * vector2.magnitude));
    if rad:
        return rads;
    else:
        return rads * 180/pi;
    
def is_vparallel(vector1, vector2):
    
    coefficient = None;
    parallel = False;
    
    for v1, v2 in zip(vector1.coordinates, vector2.coordinates):
        multiplier = None;
        if(isinstance(coefficient, NoneType)):
            if(v1 > v2):
                multiplier = v1/v2 if(v2 != 0x0) else 0x0;
            else:
                multiplier = v2/v1 if(v1 != 0x0) else 0x0;
            coefficient = multiplier;
        else:
            if(v1 > v2):
                multiplier = v1/v2 if(v2 != 0x0) else 0x0;
            else:
                multiplier = v2/v1 if(v1 != 0x0) else 0x0;
            if(coefficient == multiplier):
                parallel = True;

    return parallel;

def vprojection(vector1, vector2):
    # Projection of vector1 onto vector2;
    return vscalar_product(vdot(vector1.coordinates, vector2.unit), vector2.unit);

def is_vorthogonal(vector1, vector2):
    return vdot(vector1.coordinates, vector2.coordinates) == 0x0;

def vscalar_product(scalar, vector):
    
    vaux = [];
    for vix in vector:
        vaux.append(scalar * vix);
    return Vector(vaux);

if __name__ == '__main__':
    v1 = Vector([3.009, -6.172, 3.692, -2.51]);
    v2 = Vector([6.404, -9.144, 2.759, 8.718]);
    
    proj_v1 = vprojection(v1, v2);
    
