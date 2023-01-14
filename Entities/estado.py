from enum import Enum
class Estado(Enum):
    LIBRE = "Libre"
    OCUPADA = "Ocupada"
    ABONOLIBRE = "Libre con abono"
    ABONOOCUPADA = "Ocupada con abono"