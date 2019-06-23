#include <Arduino.h>
#define FASTLED_ESP8266_RAW_PIN_ORDER
#include <FastLED.h>
#include "main.h"
#include <ESP8266WiFi.h>

const char* ssid = "COMTECO-95193887";
const char* password = "f4m1l14C0ND322";
WiFiServer server(80);
#define NUM_LEDS 10
#define DATA_PIN 13 //D7 - MOSI
#define CLOCK_PIN 14 //D5 - CK

CRGB leds[NUM_LEDS];

void setup() {
  Serial.begin(115200);
  delay(10);
  FastLED.addLeds<WS2801, DATA_PIN, CLOCK_PIN, RGB>(leds, NUM_LEDS);
  Serial.println("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected");
  server.begin();
  Serial.println("Server started");
  Serial.print("http://");
  Serial.print(WiFi.localIP());
  Serial.println("/");
}
void loop() {
  WiFiClient client = server.available();
  if (!client) {
    return;
  }
  while(!client.available()){
    delay(1);
  }
  String request = client.readStringUntil('\r');
  client.flush();
  downAll();
  String strips = request.substring(5,NUM_LEDS+6);
  Serial.println(strips);
  for (int i = 0; i < strips.length(); i++)
  {
    switch (strips[i])
    {
    case 'r':
      leds[i]=CRGB::Red;
      break;
    case 'g':
      leds[i]=CRGB::Green;
      break;
    case 'b':
      leds[i]=CRGB::Blue;
      break; 
    case 'k':
      leds[i]=CRGB::Black;
    default:
      leds[i]=CRGB::Black;
      break;
    }
  }
  FastLED.show();
}
void downAll() 
{
  for(int dot = 0; dot < NUM_LEDS; dot++)
  {
    leds[dot] = CRGB::Black;
  }
  FastLED.show();
}

