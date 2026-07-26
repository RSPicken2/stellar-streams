from dataclasses import dataclass

@dataclass
class ExperimentInfo:
    name: str
    label: str
    unit: str
    sciNot: bool


Concentration = ExperimentInfo(name='Concentration', label=r'$W_0$', unit='', sciNot=False)
Mass          = ExperimentInfo(name='Mass', label=r'M', unit=r'$M_\odot$', sciNot=True)
HalfMass      = ExperimentInfo(name='HalfMass', label=r'$r_{\frac{1}{2}}$', unit=r'$pc$', sciNot=False)
Vx            = ExperimentInfo(name='Vx', label=r'$V_x$', unit=r'$\,km\,s^{-1}$', sciNot=False)
BinaryFrac    = ExperimentInfo(name='BinaryFrac', label=r'$F_{bin}$', unit='', sciNot=False)

GalFeatures   = ExperimentInfo(name='GalFeatures', label='', unit='', sciNot=False)


exlist = [Concentration, Mass, HalfMass, Vx, BinaryFrac, GalFeatures]