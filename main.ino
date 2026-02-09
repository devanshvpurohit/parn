#include <WiFi.h>
#include <HTTPClient.h>
#include "DHT.h"

#define DHTPIN 4
#define DHTTYPE DHT11
#define MQ135_PIN 34

DHT dht(DHTPIN, DHTTYPE);

// AP credentials
const char* ssid = "ESP32_AQI";
const char* password = "12345678";

// PC IP (connected to ESP32 AP)
const char* serverURL = "http://192.168.4.2:8501/data";

void setup() {
  Serial.begin(115200);
  dht.begin();

  WiFi.softAP(ssid, password);
  Serial.println("ESP32 AP started");
  Serial.println(WiFi.softAPIP());
}

void loop() {
  float temp = dht.readTemperature();
  float hum = dht.readHumidity();
  int mq135 = analogRead(MQ135_PIN);

  if (isnan(temp) || isnan(hum)) return;

  HTTPClient http;
  http.begin(serverURL);
  http.addHeader("Content-Type", "application/json");

  String payload = "{";
  payload += "\"temperature\":" + String(temp) + ",";
  payload += "\"humidity\":" + String(hum) + ",";
  payload += "\"mq135\":" + String(mq135);
  payload += "}";

  int code = http.POST(payload);
  http.end();

  Serial.println(payload);
  Serial.println("HTTP code: " + String(code));

  delay(5000);
}
