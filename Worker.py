'''
Created on Nov 21, 2016

@author: iaskarov
'''

import Vector;
from VectorOperations import vadd, vsubtract, vcomponent, vdot, vangle, pythagorean, sohcahtoa, vcross, is_vparallel, vprojection, is_vorthogonal, vscalar_product

if __name__ == '__main__':
    v1 = Vector([3.009, -6.172, 3.692, -2.51]);
    v2 = Vector([6.404, -9.144, 2.759, 8.718]);
    
    proj_v1 = vprojection(v1, v2);
    
    vcomp = vcomponent(v1, proj_v1);
    
    print proj_v1;
    print vcomp;
    print vadd(proj_v1, vcomp);
