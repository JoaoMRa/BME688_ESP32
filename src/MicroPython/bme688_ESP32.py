from machine import I2C
import time

class BME688:
    def __init__(self, i2c, addr=0x76):
        self.i2c = i2c
        self.addr = addr
        self._calibration_data = None
        self._is_initialized = False
        self._initialize_sensor()

    def _initialize_sensor(self):
        # Lê o ID do dispositivo
        device_id = self._read_byte(0xD0)
        if device_id != 0x61:
            raise ValueError("Sensor BME688 não encontrado!")
        self._is_initialized = True

        # Configurar o sensor para operar (opções específicas podem ser aplicadas)
        self._write_byte(0x74, 0x3F)  # Exemplo de comando para configuração (ajustar conforme necessário)
        time.sleep(0.1)

    def _read_byte(self, register):
        """ Lê um byte de um registro específico """
        return self.i2c.readfrom_mem(self.addr, register, 1)[0]

    def _write_byte(self, register, value):
        """ Escreve um byte em um registro específico """
        self.i2c.writeto_mem(self.addr, register, bytearray([value]))

    def read_sensor_data(self):
        """ Lê os dados brutos do sensor (temperatura, umidade, pressão e qualidade do ar) """
        if not self._is_initialized:
            raise ValueError("Sensor não inicializado")

        # Lê dados do sensor (ajustar os registros conforme o datasheet do BME688)
        data = self.i2c.readfrom_mem(self.addr, 0x1D, 32)  # Lê 32 bytes de dados do sensor
        return data

    def get_temperature(self):
        """ Retorna a temperatura em Celsius """
        data = self.read_sensor_data()
        # Parse os dados e converta conforme o cálculo de temperatura do BME688
        temp_raw = (data[0] << 8) | data[1]  # Exemplo de como pegar a temperatura
        return temp_raw / 100.0  # Ajustar conforme necessário

    def get_humidity(self):
        """ Retorna a umidade relativa em % """
        data = self.read_sensor_data()
        hum_raw = (data[2] << 8) | data[3]  # Exemplo de como pegar a umidade
        return hum_raw / 100.0  # Ajustar conforme necessário

    def get_pressure(self):
        """ Retorna a pressão em hPa """
        data = self.read_sensor_data()
        press_raw = (data[4] << 8) | data[5]  # Exemplo de como pegar a pressão
        return press_raw / 100.0  # Ajustar conforme necessário

    def get_gas_resistance(self):
        """ Retorna a resistência do gás (em Ohms) """
        data = self.read_sensor_data()
        gas_raw = (data[6] << 8) | data[7]  # Exemplo de como pegar a resistência do gás
        return gas_raw

    def get_air_quality_index(self):
        """ Retorna um índice simplificado de qualidade do ar """
        # A fórmula exata dependerá do seu algoritmo de qualidade do ar, mas vamos fazer uma suposição simples:
        gas_resistance = self.get_gas_resistance()
        air_quality = (gas_resistance / 1000.0)  # Ajuste conforme o algoritmo de qualidade do ar
        return air_quality
