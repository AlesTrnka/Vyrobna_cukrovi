from vyrobna import Vyrobna

# Vyrobí více různých druhů cukroví
for i in range(5):
    cukrovi = Vyrobna.zlute()
    print(cukrovi)
for i in range(6):
    cukrovi = Vyrobna.cervene()
    print(cukrovi)
for i in range(8):
    cukrovi = Vyrobna.hnede()
    print(cukrovi)