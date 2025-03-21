from bme688_esp32 import BME688_ESP32
import time

bme = BME688_ESP32()

while True:
    print(f"Temperatura: {bme.read_temperature()} °C")
    print(f"Humidade: {bme.read_humidity()} %")
    print(f"Pressão: {bme.read_pressure()} hPa")
    print(f"Resistência do Gás: {bme.read_gas_resistance()} Ohms")
    print(f"Índice de Qualidade do Ar (IAQ): {bme.read_air_quality_index()}")
    print(f"Equivalente de CO2: {bme.get_co2()}")
    print(f"Composto Orgânico Volátil (VOC): {bme.get_voc()}")
    
    time.sleep(2)  # Atualiza a cada 2 segundos
