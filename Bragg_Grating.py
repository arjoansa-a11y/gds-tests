import gdsfactory as gf
from gdsfactory.component import Component
from gdsfactory.typings import ComponentSpec, CrossSectionSpec
from gdsfactory.cross_section import Section, cross_section, CrossSection
import numpy as np
import sympy as sp
from scipy.optimize import fsolve

def neff(wavelength):
    neff = 2.4379 - 1.1193*(wavelength*1e6-1.554) - 0.0350*(wavelength*1e6-1.554)**2
    return neff

def dneff(width):
    dneff = 10.4285*(width-0.5)**3 - 5.2487*(width-0.5)**2 + 1.6142*(width-0.5)
    return dneff

Period = 310e-9
NG = 100
loss = np.log(10)*3/10*100
width1 = 0.49
width2 = 0.51

f = lambda landa: landa - Period*2*(neff(landa) + (dneff(width2) + dneff(width1))/2)
bragg_wl = fsolve(f, 1550e-9)[0]

wavelength = np.linspace(-50e-9, 50e-9, 10000) + bragg_wl 

i = 0
c = gf.Component()
for j in range(NG):

    x_wide = cross_section(width=width1, offset=i*Period, layer=(0,0))
    x_thin = cross_section(width=width2, offset=(1/2+i)*Period, layer=(0,0))

    wg_wide = gf.c.straight(length=Period*NG, cross_section=x_wide)
    c << wg_wide

    wg_thin = gf.c.straight(length=Period*NG, cross_section=x_thin)
    c << wg_thin

    i += 1

c.plot()   