from dataclasses import dataclass

@dataclass
class ExperimentInfo:
    name: str
    label: str
    unit: str
    sciNot: bool
    formattable: bool

    def FormatLabel(self, value):
        if not self.formattable: #Galfeatures dont have a numeric value to format
            return value
        if self.sciNot:
            mantissa, exponent = f"{value:.2e}".split("e")
            exponent = int(exponent)
            return fr'{self.label}$={mantissa}\times 10^{{{exponent}}}$ {self.unit}'
        else:
            return fr'{self.label}$={value}$ {self.unit}'


Concentration = ExperimentInfo(name='Concentration', label=r'$W_0$', unit='', sciNot=False, formattable=True)
Mass          = ExperimentInfo(name='Mass', label=r'M', unit=r'$M_\odot$', sciNot=True, formattable=True)
HalfMass      = ExperimentInfo(name='HalfMass', label=r'$r_{\frac{1}{2}}$', unit=r'$pc$', sciNot=False, formattable=True)
#Vx            = ExperimentInfo(name='Vx', label=r'$V_x$', unit=r'$\,km\,s^{-1}$', sciNot=False, formattable=True)
Periapsis     = ExperimentInfo(name='Periapsis', label=r'$r_p$', unit='$kpc$', scinot=False, formattable=True)
BinaryFrac    = ExperimentInfo(name='BinaryFrac', label=r'$F_{bin}$', unit='', sciNot=False, formattable=True)
GalacticMass  = ExperimentInfo(name='GalacticMass', label=r'$M_d$', unit='$M_\odot$', sciNot=True, formattable=True)

GalFeatures   = ExperimentInfo(name='GalFeatures', label='', unit='', sciNot=False, formattable=False)


exlist = [Concentration, Mass, HalfMass, Periapsis, BinaryFrac, GalacticMass, GalFeatures]

exdict = {e.name: e for e in exlist}

def get_experiment_info(name):
    try:
        return exdict[name]
    except KeyError:
        raise ValueError(f"No ExperimentInfo found for name: {name}")
