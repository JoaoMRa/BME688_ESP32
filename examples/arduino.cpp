#include <Wire.h>
#include "BME688_ESP32.h"

BME688 sensor;  // Cria o objeto do sensor BME688

void setup() {
  Serial.begin(115200);
  if (!sensor.begin()) {
    Serial.println("Falha ao inicializar o BME688");
    while (1);
  }
  Serial.println("Sensor BME688 inicializado com sucesso!");
}

void loop() {
  if (sensor.readSensorData()) {
    Serial.print("Temperatura: ");
    Serial.print(sensor.getTemperature());
    Serial.print(" °C, ");
    Serial.print("Umidade: ");
    Serial.print(sensor.getHumidity());
    Serial.print(" %, ");
    Serial.print("Pressão: ");
    Serial.print(sensor.getPressure());
    Serial.print(" hPa, ");
    Serial.print("Gas Resistance: ");
    Serial.print(sensor.getGasResistance());
    Serial.print(" Ohms, ");
    Serial.print("Índice de Qualidade do Ar: ");
    Serial.println(sensor.getAirQualityIndex());
  } else {
    Serial.println("Dados não prontos.");
  }
  delay(1000);
}
