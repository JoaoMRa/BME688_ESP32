#ifndef BME688_H
#define BME688_H

#include <Wire.h>   // Para I2C (dependendo da plataforma)
#include <SPI.h>    // Para SPI (se necessário)
#include <stdint.h>

class BME688 {
public:
    // Construtor
    BME688(uint8_t i2cAddress = 0x76);  // Endereço I2C padrão

    // Funções de inicialização
    bool begin();  // Inicializa o sensor (I2C ou SPI)
    bool beginSPI(uint8_t csPin);  // Inicializa via SPI (se necessário)

    // Funções de leitura
    bool readSensorData();
    float getTemperature();
    float getHumidity();
    float getPressure();
    float getGasResistance();
    float getAirQualityIndex();

private:
    uint8_t _address;  // Endereço I2C
    uint8_t _csPin;    // Pino SPI CS
    uint8_t _spiMode;  // SPI Mode (se necessário)
    bool _isSPI;       // Determina se está usando SPI

    // Funções de controle de leitura e escrita do sensor
    uint8_t readByte(uint8_t reg);
    void writeByte(uint8_t reg, uint8_t value);

    // Funções internas de processamento
    void initializeSensor();
    void readCalibrationData();
    bool isDataReady();
    void readRawData();
};
#endif
