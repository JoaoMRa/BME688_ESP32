# BME688_ESP32

Library for interacting with the **BME688** sensor from **Bosch** on **ESP32** boards, compatible with both **Arduino** and **MicroPython**. The BME688 sensor provides measurements for **temperature**, **humidity**, **pressure**, and **gas resistance**, as well as an air quality index, making it ideal for IoT and environmental monitoring projects.

## 🚀 Features
- Reads **temperature**, **humidity**, **pressure**, and **gas resistance**.
- Provides **air quality index** based on gas resistance.
- Compatible with **Arduino** (ESP32) and **MicroPython** on ESP32 boards.
- Easy-to-use API for both platforms.

## 📦 Installation

### For **Arduino**
1. Download or clone this repository.
2. Copy the `BME688_ESP32` folder into your **Arduino libraries** folder (`~/Documents/Arduino/libraries/`).
3. Restart the **Arduino IDE**.

### For **MicroPython**
1. Upload the `bme688_esp32.py` file to your **ESP32** using **Thonny** or **mpy-cross**.
2. Import the library in your MicroPython code:

```python
from bme688_esp32 import BME688_ESP32
```
## 📖 Usage Examples
### 🟢 Basic Example (Arduino)
```c++

#include "BME688_ESP32.h"

HardwareSerial mySerial(1);
BME688_ESP32 bme(mySerial);

void setup() {
  Serial.begin(115200);
  mySerial.begin(9600, SERIAL_8N1, 17, 16); // Adjust serial pins (TX, RX) if needed
  bme.begin();
}

void loop() {
  // Get temperature in Celsius
  float temperature = bme.readTemperature();
  // Get humidity in percentage
  float humidity = bme.readHumidity();
  // Get pressure in hPa
  float pressure = bme.readPressure();
  // Get gas resistance in Ohms
  float gasResistance = bme.readGasResistance();
  // Get air quality index
  float airQuality = bme.readAirQualityIndex();

  Serial.print("Temperature: ");
  Serial.println(temperature);
  Serial.print("Humidity: ");
  Serial.println(humidity);
  Serial.print("Pressure: ");
  Serial.println(pressure);
  Serial.print("Gas Resistance: ");
  Serial.println(gasResistance);
  Serial.print("Air Quality: ");
  Serial.println(airQuality);

  delay(1000);  // Update every second
}
```
### 🟢 Basic Example (MicroPython)
```python

from bme688_esp32 import BME688_ESP32
import time

# Initialize BME688
bme = BME688_ESP32(i2c_id=0, baudrate=115200, tx=17, rx=16)

# Initialize sensor
bme.begin()

while True:
    # Read temperature, humidity, pressure, gas resistance, and air quality
    temperature = bme.read_temperature()
    humidity = bme.read_humidity()
    pressure = bme.read_pressure()
    gas_resistance = bme.read_gas_resistance()
    air_quality = bme.read_air_quality_index()

    print(f"Temperature: {temperature} C")
    print(f"Humidity: {humidity} %")
    print(f"Pressure: {pressure} hPa")
    print(f"Gas Resistance: {gas_resistance} Ohms")
    print(f"Air Quality: {air_quality}")

    time.sleep(1)
```

## 🛠 Sensor Function Reference
Here’s a table of the main functions available in the BME688_ESP32 library to interact with the BME688 sensor:

| **Function**                     | **Description**                                                         |
|-----------------------------------|-------------------------------------------------------------------------|
| `begin()`                         | Initializes the sensor and prepares it for measurements. Should be called in `setup()`. |
| `readTemperature()`               | Reads the temperature (in Celsius) from the BME688 sensor.              |
| `readHumidity()`                  | Reads the humidity (in %) from the BME688 sensor.                      |
| `readPressure()`                  | Reads the pressure (in hPa) from the BME688 sensor.                     |
| `readGasResistance()`             | Reads the gas resistance (in Ohms) from the BME688 sensor.              |
| `readAirQualityIndex()`           | Calculates and returns the air quality index based on gas resistance.   |
| `getTemperatureF()`               | Returns temperature in Fahrenheit (converts from Celsius).              |
| `getHumidityPercentage()`         | Returns the humidity as a percentage.                                   |
| `getPressureInHg()`               | Returns pressure in inches of mercury (inHg).                           |
| `getGasResistanceInOhms()`        | Returns the gas resistance in Ohms.                                     |


