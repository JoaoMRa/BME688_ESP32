# BME688_ESP32

Library for interacting with the **BME688** sensor from **Bosch** on **ESP32** boards, compatible with **Arduino** and **MicroPython**. Now integrated with Bosch's **BSEC 2.5.0** for advanced data processing, including **neural network** for detecting gas patterns and air quality prediction.

## 🚀 Features
- Read **temperature**, **humidity**, **pressure**, and **gas resistance**.
- Calculate the **Air Quality Index (IAQ)** using Bosch's **BSEC 2.5.0** library.
- Predict **CO2 equivalent (eCO2)** and **Volatile Organic Compounds (VOC)**.
- Supports Bosch's integrated **neural network**, enabling detection of complex gas patterns.
- Compatible with **Arduino** (ESP32) and **MicroPython**.

## 📦 Installation

### For **Arduino**
1. Download or clone this repository.
2. Copy the `BME688_ESP32` folder into your **Arduino libraries** folder (`~/Documents/Arduino/libraries/`).
3. Install the Bosch **BSEC 2.5.0** library for advanced sensor processing:
   - Open the **Arduino IDE**.
   - Go to **Sketch > Include Library > Manage Libraries**.
   - Search for **BSEC** and install **Bosch BSEC** by **Bosch Sensortec**.
4. Restart the **Arduino IDE**.

### For **MicroPython**
1. Upload the `bme688_esp32.py` file to your **ESP32** using **Thonny** or **mpy-cross**.
2. Install the Bosch **BSEC 2.5.0** library for MicroPython (check Bosch's documentation for installation steps).
3. Import the library in your MicroPython code:
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