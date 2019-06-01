#include <Arduino.h>
#include <FastLED.h>

#define NUM_LEDS 16
#define DATA_PIN 13
#define CLOCK_PIN 11

CRGB leds[NUM_LEDS];


void downAll();
void setup() { 
      // Uncomment/edit one of the following lines for your leds arrangement.
      // FastLED.addLeds<TM1803, DATA_PIN, RGB>(leds, NUM_LEDS);
      // FastLED.addLeds<TM1804, DATA_PIN, RGB>(leds, NUM_LEDS);
      // FastLED.addLeds<TM1809, DATA_PIN, RGB>(leds, NUM_LEDS);
      // FastLED.addLeds<WS2811, DATA_PIN, RGB>(leds, NUM_LEDS);
      // FastLED.addLeds<WS2812, DATA_PIN, RGB>(leds, NUM_LEDS);
      // FastLED.addLeds<WS2812B, DATA_PIN, RGB>(leds, NUM_LEDS);
      // FastLED.addLeds<NEOPIXEL, DATA_PIN, RGB>(leds, NUM_LEDS);
      // FastLED.addLeds<UCS1903, DATA_PIN, RGB>(leds, NUM_LEDS);
      // FastLED.addLeds<SM16716, RGB>(leds, NUM_LEDS);
      // FastLED.addLeds<LPD8806, RGB>(leds, NUM_LEDS);
      FastLED.addLeds<WS2801, DATA_PIN, CLOCK_PIN, RGB>(leds, NUM_LEDS);
      // FastLED.addLeds<SM16716, DATA_PIN, CLOCK_PIN, RGB>(leds, NUM_LEDS);
      // FastLED.addLeds<LPD8806, DATA_PIN, CLOCK_PIN, RGB>(leds, NUM_LEDS);
      //FastLED.addLeds<WS2801, RGB>(leds, NUM_LEDS); //we're using WS2801
}
void loop() { 
    for(int dot = 0; dot < NUM_LEDS; dot++)
    {
      downAll();
      // leds[dot].red=52;
      // leds[dot].green=153;
      // leds[dot].blue=3;
      leds[dot]=CRGB::Green;
      FastLED.show();
      delay(1000);
    }
}
void downAll(){
  for(int dot = 0; dot < NUM_LEDS; dot++)
  {
    leds[dot] = CRGB::Black;
  }
  FastLED.show();
}


