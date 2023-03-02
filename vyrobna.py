from cukrovi import Cukrovi

class Vyrobna():
    """ Třída se statickými metodami pro výrobu různých druhů cukroví."""
    
    @staticmethod
    def zlute():
        return Cukrovi("žlutá", "kulatý", 30)

    @staticmethod
    def cervene():
        return Cukrovi("červená", "kulatý", 35)

    @staticmethod
    def hnede():
        return Cukrovi("hnědá", "hranatý", 10)