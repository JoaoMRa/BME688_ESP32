import time
from machine import I2C, Pin
from bme688_ESP32 import BME688_ESP32

# Inicializar o I2C (ajuste os pinos conforme a sua placa)
i2c = I2C(0, scl=Pin(22), sda=Pin(21))  # Exemplo para ESP32

# Criar o objeto BME688
sensor = BME688_ESP32(i2c)

# Loop principal
while True:
    try:
        # Ler os dados dos sensores
        temp = sensor.get_temperature()
        hum = sensor.get_humidity()
        press = sensor.get_pressure()
        gas = sensor.get_gas_resistance()
        air_quality = sensor.get_air_quality_index()

        # Exibir os dados no terminal
        print(f"Temperatura: {temp} C")
        print(f"Umidade: {hum} %")
        print(f"Pressão: {press} hPa")
        print(f"Resistência do Gás: {gas} Ohms")
        print(f"Índice de Qualidade do Ar: {air_quality}")
        print("-" * 30)

    except ValueError as e:
        print(f"Erro: {e}")
    
    time.sleep(2)  # Espera 2 segundos antes de fazer a próxima leitura
