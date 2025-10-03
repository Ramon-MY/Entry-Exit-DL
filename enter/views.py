import random

def readData():
    """
    Función simulada para devolver un ID de tarjeta RFID.
    En lugar de leer un lector real, generamos un ID aleatorio.
    """
    # Lista de IDs simulados
    fake_ids = ["RFID1001", "RFID1002", "RFID1003", "RFID1004", "RFID1005"]
    
    # Elegir un ID al azar cada vez que se llama
    return random.choice(fake_ids)

