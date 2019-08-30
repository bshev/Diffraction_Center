import numpy as np
import os

aff_dict = np.load(os.path.join('Atomic_Form_Factors','Atomic_Form_Factor_Dictionary.npy'),allow_pickle=True).item()
    
def FormFactor(q,elem): 
    ''' 
    Loads atomic form factor function from tabulated data. 
    Element can be symbol or atomic number e.g. 'C' or 6. 
    Lengths (or inverse lengths) are in Angstroms
    '''
    a = aff_dict[elem][1]
    coeff = a[1:]
    coeff = np.array([coeff[0:5],coeff[5:10]])
    val = coeff[0,0]*np.exp(-coeff[1,0]*((q/(2*np.pi))**2)) + coeff[0,1]*np.exp(-coeff[1,1]*((q/(2*np.pi))**2)) + coeff[0,2]*np.exp(-coeff[1,2]*((q/(2*np.pi))**2)) + coeff[0,3]*np.exp(-coeff[1,3]*((q/(2*np.pi))**2)) + coeff[0,4]*np.exp(-coeff[1,4]*((q/(2*np.pi))**2))
    return val