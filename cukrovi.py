class Cukrovi():
    """Třída pro inicializaci instancí cukroví"""
    
    barva = None
    tvar = None
    vaha = 0

    def __init__(self, barva, tvar, vaha):
        self.barva = barva
        self.tvar = tvar
        self.vaha = vaha
        
    def __str__(self):
        return f"Cukroví má tvar {self.tvar}, barvu {self.barva} a váží {self.vaha}." 