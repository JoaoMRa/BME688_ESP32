# BME688_ESP32

Biblioteca para interação com o sensor **BME688** da **Bosch** em placas **ESP32**, compatível com **Arduino** e **MicroPython**. Agora integrada com a **BSEC 2.5.0** da Bosch para processamento avançado de dados, incluindo **rede neural** para detecção de padrões de gases e previsão da qualidade do ar.

## 🚀 Funcionalidades
- Leitura de **temperatura**, **umidade**, **pressão** e **resistência de gás**.
- Cálculo do **índice de qualidade do ar (IAQ)** usando a biblioteca **BSEC 2.5.0** da Bosch.
- Predição de **CO2 equivalente (eCO2)** e **Compostos Orgânicos Voláteis (VOC)**.
- Suporte à **rede neural integrada da Bosch**, que permite detectar padrões complexos de gases.
- Compatível com **Arduino** (ESP32) e **MicroPython**.

## 📦 Instalação

### Para **Arduino**
1. Baixe ou clone este repositório.
2. Faça o download da **BSEC 2.5.0** da Bosch:  
   - [Bosch BSEC Library](https://www.bosch-sensortec.com/software-tools/software/previous-bsec-software-versions/)
3. Copie a pasta `BME688_ESP32` e os arquivos da **BSEC** para a pasta de bibliotecas do Arduino (`~/Documents/Arduino/libraries/`).
4. Reinicie a **IDE do Arduino**.

### Para **MicroPython**
1. Baixe a **BSEC** da Bosch e os arquivos necessários.
2. Suba o arquivo `bme688_esp32.py` para o ESP32 via **Thonny** ou **mpy-cross**.
3. No código MicroPython, importe a biblioteca:
```python
from bme688_esp32 import BME688_ESP32
```

## 📖 Exemplos de Uso
### 🟢 Exemplo Básico (Arduino)
```cpp

#include "BME688_ESP32.h"

BME688_ESP32 bme;

void setup() {
    Serial.begin(115200);
    
    if (!bme.begin()) {
        Serial.println("Erro ao inicializar o BME688!");
        while (1);
    }
    Serial.println("BME688 inicializado!");
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

    Serial.print("CO2 Equivalente: ");
    Serial.println(bme.getCO2());

    Serial.print("VOC Equivalente: ");
    Serial.println(bme.getVOC());

    delay(2000);
}
```
### 🟢 Exemplo Básico (MicroPython)
```python

from bme688_esp32 import BME688_ESP32
import time

bme = BME688_ESP32()

while True:
    print(f"Temperatura: {bme.read_temperature()} °C")
    print(f"Humidade: {bme.read_humidity()} %")
    print(f"Pressão: {bme.read_pressure()} hPa")
    print(f"Resistência do Gás: {bme.read_gas_resistance()} Ohms")
    print(f"Índice de Qualidade do Ar (IAQ): {bme.read_air_quality_index()}")
    print(f"CO2 Equivalente: {bme.get_co2()}")
    print(f"VOC Equivalente: {bme.get_voc()}")
    
    time.sleep(2)
```

## 🛠 Funções da Biblioteca

| Função                  | Descrição                                                                 |
|-------------------------|---------------------------------------------------------------------------|
| `begin()`               | Inicializa o sensor e configura a BSEC.                                  |
| `readTemperature()`     | Retorna a temperatura em °C.                                              |
| `readHumidity()`        | Retorna a umidade relativa em %.                                          |
| `readPressure()`        | Retorna a pressão atmosférica em hPa.                                     |
| `readGasResistance()`   | Retorna a resistência de gás em Ohms.                                     |
| `readAirQualityIndex()` | Calcula e retorna o Índice de Qualidade do Ar (IAQ).                      |
| `getCO2()`              | Retorna a estimativa de CO2 equivalente (eCO2).                            |
| `getVOC()`              | Retorna a estimativa de Compostos Orgânicos Voláteis (VOC).               |

## 🔗 Referências
### GitHub Repositório: BME688_ESP32
### BSEC da Bosch: Bosch Sensortec
### MicroPython: micropython.org
### Arduino ESP32: arduino.cc
## ✉️ Maintainer: João Moreira