'''
Created on Nov 21, 2016

@author: iaskarov
'''

from Vector import Vector;
from VectorOperations import vadd, vsubtract, vcomponent, vdot, vangle, pythagorean, sohcahtoa, vcross, is_vparallel, vprojection, is_vorthogonal, vscalar_product

if __name__ == '__main__':
    v1 = Vector([1.5, 9.547, 3.691]);
    v2 = Vector([-6.007, 0.124, 5.772]);
    
    cross = vcross(v1.coordinates, v2.coordinates);
    print cross.magnitude/2;
    
    
    
    
