from machine import I2C, Pin
import time
import bme68x

class BME688_ESP32:
    def __init__(self, i2c_id=0, scl=22, sda=21, freq=400000):
        self.i2c = I2C(i2c_id, scl=Pin(scl), sda=Pin(sda), freq=freq)
        self.sensor = bme68x.BME68X(self.i2c)

    def read_temperature(self):
        return self.sensor.get_temperature()

    def read_humidity(self):
        return self.sensor.get_humidity()

    def read_pressure(self):
        return self.sensor.get_pressure()

    def read_gas_resistance(self):
        return self.sensor.get_gas_resistance()

    def read_air_quality_index(self):
        return self.sensor.get_air_quality_index()
    
    def get_iaq(self):
        return self.sensor.get_iaq()

    def get_co2(self):
        return self.sensor.get_co2_equivalent()

    def get_voc(self):
        return self.sensor.get_breath_voc_equivalent()
