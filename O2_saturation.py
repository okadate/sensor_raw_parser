# encoding: utf-8

import numpy as np


def O2_saturation(T, S, convert_mg=True, method='BK84'):
    """
    Return saturation value of oxygen.
    
    Parameters
    ----------
    T : array_like
        Temperature (˚C)
    S : array_like
        Salinity (PSU)
    
    Returns
    -------
    O2_sat : array_like
        concentrations of O2 [ millimole O2 / m3 ] for a given temperature and
        salinity (at STP)
    """

    # Weiss 1970 (pyroms)
    if method=='W70':
        A1 = -173.4292
        A2 =  249.6339
        A3 =  143.3483
        A4 =  -21.8492
        B1 =   -0.033096
        B2 =    0.014259
        B3 =   -0.0017000
        Ts = T + 273.15
        # O2 Concentration in ml/l
        # [from Millero and Sohn, Chemical Oceanography, CRC Press, 1992]
        lnO = A1 + A2*(100.0/Ts) + A3*np.log(Ts/100.0) + A4*(Ts/100.0) \
            + S * (B1 + B2*(Ts/100.0) + B3*((Ts/100.0)**2))
        O = np.exp(lnO)
    
    # Benson and Krause 1984
    elif method=='BK84':
        A0 = -135.29996
        A1 =  1.572288e5
        A2 = -6.637149e7
        A3 =  1.243678e10
        A4 = -8.621061e11
        B0 =  0.020573
        B1 = -12.142
        B2 =  2363.1
        Ts = T + 273.15
        # O2 Concentration in umol/l
        # [from Millero and Sohn, Chemical Oceanography, CRC Press, 1992]
        lnO = A0 + A1/Ts + A2/(Ts**2) + A3/(Ts**3) + A4/(Ts**4) \
            - S*(B0 + B1/Ts + B2/(Ts**2))
        O = np.exp(lnO) / 44.66
        
    # Garcia and Gordon 1992
    elif method=='GG92':
        Ts = np.log((298.15-T)/(273.15+T))
        A0 =  2.00907
        A1 =  3.22014
        A2 =  4.0501
        A3 =  4.94457
        A4 = -0.256847
        A5 =  3.88767
        B0 = -0.00624523
        B1 = -0.00737614
        B2 = -0.010341
        B3 = -0.00817083
        C0 = -0.000000488682
        lnO = A0 + A1*Ts + A2*(Ts**2) + A3*(Ts**3) + A4*(Ts**4) + A5*(Ts**5) \
            + S * (B0 + B1*Ts + B2*(Ts**2) + B3*(Ts**3)) \
            + C0 * (S**2)
        O = np.exp(lnO)
    
    # O ml/l
    # 44.66 l/mol
    # 22.4 l/mol 
    # 1.42903 g/l
    if convert_mg:
        return O * 1.42903      # mg/l
    else:
        return O / 22.4 * 1000  # mmol/m3


if __name__ == '__main__':
    
    T = 30.
    S = 35.
    print(T, S, O2_saturation(T, S, method='W70', convert_mg=True),  O2_saturation(T, S, method='W70', convert_mg=False))
    print(T, S, O2_saturation(T, S, method='BK84', convert_mg=True), O2_saturation(T, S, method='BK84', convert_mg=False))
    print(T, S, O2_saturation(T, S, method='GG92', convert_mg=True), O2_saturation(T, S, method='GG92', convert_mg=False))
