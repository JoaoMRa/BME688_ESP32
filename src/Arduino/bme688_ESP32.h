#ifndef BME688_ESP32_H
#define BME688_ESP32_H

#include <Arduino.h>
#include <Wire.h>
#include "bsec.h"

class BME688_ESP32 {
public:
    BME688_ESP32(uint8_t i2c_addr = 0x76, TwoWire &wirePort = Wire);
    
    bool begin();
    float readTemperature();
    float readHumidity();
    float readPressure();
    float readGasResistance();
    float readAirQualityIndex();

    // Functions using BSEC
    bool runBSEC();
    float getIAQ();  
    float getCO2();
    float getVOC();

private:
    uint8_t _i2c_addr;
    TwoWire *_wire;
    Bsec iaqSensor;
    bsec_bme_settings_t sensor_settings;
};

#endif
