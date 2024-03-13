# Comportamientos de ataque
def espaditas():
    print("Ataque con espada.")

def arco_ataque():
    print("Disparo de flecha.")

def ataque_lanza():
    print("Carga con lanza.")

# Comportamientos de movimiento
def caminata():
    print("Caminan.")

def sigiloso():
    print("Se mueven en cunclillas.")

def trotamiento():
    print("Trota.")

# Unidad militar
class MilitaryUnit:
    def __init__(self, attack_behavior, movement_behavior):
        self.attack_behavior = attack_behavior
        self.movement_behavior = movement_behavior

    def perform_attack(self):
        self.attack_behavior()

    def perform_movement(self):
        self.movement_behavior()

# Mapa de comportamientos
attack_behaviors = {
    "Soldadito": espaditas,
    "Bowlsai": arco_ataque,
    "Ballaquero": ataque_lanza
}

movement_behaviors = {
    "Soldadito": caminata,
    "Bowlsai": sigiloso,
    "Ballaquero": trotamiento
}

# Ejemplo de uso
Soldadito = MilitaryUnit(attack_behaviors["Soldadito"], movement_behaviors["Soldadito"])
Bowlsai = MilitaryUnit(attack_behaviors["Bowlsai"], movement_behaviors["Bowlsai"])
Ballaquero = MilitaryUnit(attack_behaviors["Ballaquero"], movement_behaviors["Ballaquero"])

# Acciones de las unidades
Soldadito.perform_attack()
Soldadito.perform_movement()

Bowlsai.perform_attack()
Bowlsai.perform_movement()

Ballaquero.perform_attack()
Ballaquero.perform_movement()