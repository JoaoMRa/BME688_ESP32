#include "BME688_ESP32.h"

BME688_ESP32::BME688_ESP32(uint8_t i2c_addr, TwoWire &wirePort) {
    _i2c_addr = i2c_addr;
    _wire = &wirePort;
}

bool BME688_ESP32::begin() {
    _wire->begin();
    iaqSensor.begin(BME68X_I2C_ADDR_LOW, *_wire);
    if (!iaqSensor.run()) return false;
    return true;
}

float BME688_ESP32::readTemperature() {
    return iaqSensor.temperature;
}

float BME688_ESP32::readHumidity() {
    return iaqSensor.humidity;
}

float BME688_ESP32::readPressure() {
    return iaqSensor.pressure;
}

float BME688_ESP32::readGasResistance() {
    return iaqSensor.gasResistance;
}

float BME688_ESP32::readAirQualityIndex() {
    return iaqSensor.iaq;
}

bool BME688_ESP32::runBSEC() {
    if (iaqSensor.run()) return true;
    return false;
}

float BME688_ESP32::getIAQ() {
    return iaqSensor.iaq;
}

float BME688_ESP32::getCO2() {
    return iaqSensor.co2Equivalent;
}

float BME688_ESP32::getVOC() {
    return iaqSensor.breathVocEquivalent;
}
