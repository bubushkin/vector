'''
Created on Nov 22, 2016

@author: iaskarov
'''

from math import fsum, sqrt, pow, fabs, acos, pi, sin, tan, cos;
from types import NoneType;
import Vector;

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

def pythagorean(hypothenus=None, opposite=None, adjacent=None):
    
    if(isinstance(hypothenus, NoneType)):
        return sqrt(pow(opposite, 0x02) + pow(adjacent, 0x02));
    if(isinstance(opposite, NoneType)):
        return sqrt(pow(hypothenus, 0x02) - pow(adjacent, 0x02));
    if(isinstance(adjacent, NoneType)):
        return sqrt(pow(hypothenus, 0x02) - pow(opposite, 0x02));

def sohcahtoa(hypothenus=None, opposite=None, adjacent=None, trig="sin", rad=False):
    
    
    thetha = None;
    if(trig == 'sin'):
        
    
    if(rad):

def vcross(vector1, vector2):
    pass;
    
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
