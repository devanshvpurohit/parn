## 📌 Features

* ESP32 runs in **Access Point (AP) mode**
* Real-time air quality monitoring
* Temperature & humidity compensation
* Estimated AQI classification
* Interactive Streamlit dashboard
* Offline & self-contained
* Ideal for **college projects & demos**

---

## 🧠 System Architecture

```
MQ135 + DHT11
      ↓
   ESP32 (AP Mode)
      ↓  HTTP POST
 Streamlit Dashboard (PC)
```

---

## 🔧 Hardware Requirements

| Component                 | Quantity |
| ------------------------- | -------- |
| ESP32 Dev Board           | 1        |
| MQ135 Gas Sensor          | 1        |
| DHT11 Sensor              | 1        |
| Breadboard & Jumper Wires | —        |

---

## 🔌 Sensor Connections

| Sensor     | ESP32 Pin |
| ---------- | --------- |
| MQ135 AO   | GPIO 34   |
| DHT11 DATA | GPIO 4    |
| VCC        | 3.3V      |
| GND        | GND       |

---

## 📡 Network Configuration

| Parameter  | Value         |
| ---------- | ------------- |
| ESP32 SSID | `ESP32_AQI`   |
| Password   | `12345678`    |
| ESP32 IP   | `192.168.4.1` |
| PC IP      | `192.168.4.2` |
| Port       | `8501`        |

> ⚠️ The PC **must connect to the ESP32 Wi-Fi network**.

---

## 🧪 AQI Classification (Estimated)

| MQ135 Value | AQI Level |
| ----------- | --------- |
| < 200       | Good      |
| 200 – 399   | Moderate  |
| 400 – 599   | Unhealthy |
| ≥ 600       | Hazardous |

> ⚠️ MQ135 does **not provide true AQI**. Values are **estimated** and require calibration for accuracy.

---

## 💻 Software Requirements

### ESP32

* Arduino IDE
* ESP32 Board Package
* Libraries:

  * `WiFi.h`
  * `HTTPClient.h`
  * `DHT sensor library`

### PC (Dashboard)

```bash
pip install streamlit pandas plotly
```

---

## ▶️ How to Run

### 1️⃣ Upload ESP32 Code

* Flash the ESP32 with the AP-mode sketch
* ESP32 will create Wi-Fi: `ESP32_AQI`

---

### 2️⃣ Connect PC to ESP32 Wi-Fi

```
SSID: ESP32_AQI
Password: 12345678
```

Assign static IP if needed:

```
IP: 192.168.4.2
Gateway: 192.168.4.1
```

---

### 3️⃣ Run Streamlit Dashboard

```bash
streamlit run streamlit_app.py --server.address 192.168.4.2
```

Open browser:

```
http://192.168.4.2:8501
```

---

## 📊 Dashboard Features

* Live sensor readings
* AQI status indicator
* Interactive plots:

  * MQ135 gas levels
  * Temperature trends
  * Humidity trends
* Raw data table view

---

## 📁 Project Structure

```
ESP32_AQI_Project/
│
├── esp32_aqi.ino
├── streamlit_app.py
└── README.md
```

---

## ⚠️ Limitations

* AQI is **approximate**
* Data stored in memory (resets on restart)
* Streamlit not designed for high-throughput APIs

---

## 🚀 Future Enhancements

* CSV / SQLite data logging
* True AQI calculation (PPM → AQI)
* Sensor calibration interface
* Mobile-responsive UI
* Cloud deployment
* AQI gauge meter

---

## 🎓 Use Cases

* College mini / major projects
* IoT demonstrations
* Offline environmental monitoring
* Smart city prototypes

---

## 👨‍💻 Author

Developed using **ESP32 + Python + Streamlit**
Feel free to modify, extend, and improve 🚀

