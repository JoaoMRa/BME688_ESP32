# BME688 Library for MicroPython and Arduino (ESP32)

This is a simple library to interact with the **BME688** sensor from **Bosch**. It supports both **MicroPython** (for platforms like ESP32) and **Arduino (ESP32)**. The BME688 sensor provides temperature, humidity, pressure, and air quality readings, making it ideal for IoT projects and environmental monitoring.

## Features

- Temperature reading (in Celsius)
- Humidity reading (%)
- Pressure reading (hPa)
- Gas resistance reading (Ohms)
- Air quality index based on gas resistance

## Platforms Supported

- **MicroPython** (ESP32)
- **Arduino** (ESP32)

## Installation

### MicroPython Installation

1. Clone the repository or download the files to your device:
    ```bash
    git clone https://github.com/your-username/bme688-micropython.git
    ```

2. Import the library in your code:
    ```python
    from bme688 import BME688_ESP32
    ```

3. Make sure the **BME688** sensor is connected via **I2C** to your development board.

### Arduino (ESP32) Installation

1. Clone the repository or download the files to your local machine:
    ```bash
    git clone https://github.com/your-username/bme688-arduino.git
    ```

2. Install the necessary libraries in the Arduino IDE. You might need the **Wire** library for I2C communication and a compatible **BME688** library for Arduino (you can use the **Adafruit BME680** library as a base).

3. Include the library in your Arduino sketch:
    ```cpp
    #include "BME688.h"
    ```

4. Upload the code to your ESP32 board using the Arduino IDE.

## Usage Example

### MicroPython Example

```python
import time
from machine import I2C, Pin
from bme688 import BME688

# Initialize I2C (adjust pins for your board)
i2c = I2C(0, scl=Pin(22), sda=Pin(21))  # Example for ESP32

# Create the BME688 object
sensor = BME688(i2c)

# Main loop
while True:
    try:
        # Read sensor data
        temp = sensor.get_temperature()
        hum = sensor.get_humidity()
        press = sensor.get_pressure()
        gas = sensor.get_gas_resistance()
        air_quality = sensor.get_air_quality_index()

        # Display data in the terminal
        print(f"Temperature: {temp} C")
        print(f"Humidity: {hum} %")
        print(f"Pressure: {press} hPa")
        print(f"Gas Resistance: {gas} Ohms")
        print(f"Air Quality Index: {air_quality}")
        print("-" * 30)

    except ValueError as e:
        print(f"Error: {e}")
    
    time.sleep(2)  # Wait 2 seconds before the next reading
```
### Arduino Example

```c++
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME680.h>

Adafruit_BME680 bme;

void setup() {
  Serial.begin(115200);
  
  if (!bme.begin()) {
    Serial.println("Error initializing BME680 sensor.");
    while (1);
  }
  
  Serial.println("BME680 sensor initialized.");
}

void loop() {
  if (bme.performReading()) {
    Serial.print("Temperature: ");
    Serial.print(bme.temperature);
    Serial.println(" °C");

    Serial.print("Humidity: ");
    Serial.print(bme.humidity);
    Serial.println(" %");

    Serial.print("Pressure: ");
    Serial.print(bme.pressure / 100.0);
    Serial.println(" hPa");

    Serial.print("Gas Resistance: ");
    Serial.print(bme.gas_resistance);
    Serial.println(" Ohms");

    delay(2000); // Wait 2 seconds before the next reading
  }
}
```
## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing
Feel free to contribute! If you find a bug or want to add a feature, please open an issue or submit a pull request.

Credits
MicroPython: https://micropython.org/

Arduino ESP32: https://www.arduino.cc/

BME688: https://www.bosch-sensortec.com/productsenvironmental-sensors/bme680
