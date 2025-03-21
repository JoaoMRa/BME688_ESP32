#include "BME688_ESP32.h"

BME688_ESP32 bme;  // Criar instância do sensor

void setup() {
    Serial.begin(115200);
    
    if (!bme.begin()) {
        Serial.println("Falha ao inicializar o BME688!");
        while (1);
    }
    Serial.println("BME688 inicializado com sucesso!");
}

void loop() {
    Serial.print("Temperatura: ");
    Serial.print(bme.readTemperature());
    Serial.println(" °C");

    Serial.print("Humidade: ");
    Serial.print(bme.readHumidity());
    Serial.println(" %");

    Serial.print("Pressão: ");
    Serial.print(bme.readPressure());
    Serial.println(" hPa");

    Serial.print("Resistência do Gás: ");
    Serial.print(bme.readGasResistance());
    Serial.println(" Ohms");

    Serial.print("Índice de Qualidade do Ar (IAQ): ");
    Serial.println(bme.readAirQualityIndex());

    Serial.print("Equivalente de CO2: ");
    Serial.println(bme.getCO2());

    Serial.print("Composto Orgânico Volátil (VOC): ");
    Serial.println(bme.getVOC());

    delay(2000);  // Atualiza a cada 2 segundos
}

