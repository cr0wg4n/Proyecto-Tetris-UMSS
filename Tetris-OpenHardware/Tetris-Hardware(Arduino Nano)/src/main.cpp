#include <Arduino.h>
#include <FastLED.h>

#define NUM_LEDS 160
#define DATA_PIN 10
#define CLOCK_PIN 9

CRGB leds[NUM_LEDS];
const char *strip="bbkkkkkkkkkkkkkkkkkkkkkkkkkkkkbbkkkkkkkkkkkkkkkkkkkkkkkkkkkkkggggkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkrkkkkkkkkrrkkkkkkkkkkkkkkkkkkkkkrkkkkkkkkkkkkkkkkkkkk";

void downAll();

void setup() 
{ 
  Serial.begin(9600);
  FastLED.addLeds<WS2801, DATA_PIN, CLOCK_PIN, RGB>(leds, NUM_LEDS);
}
void loop()
{ 
  downAll();
  for (int i = 0; i < strlen(strip); i++)
  {
    switch (strip[i])
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
  delay(100);
  
    // for(int dot = 0; dot < NUM_LEDS; dot++)
    // {
    //   downAll();
    //   //leds[dot].red=127;
    //   //leds[dot].green=127;
    //   //leds[dot].blue=127;
    //   leds[dot]=CRGB::Red;
    //   FastLED.show();
    // }
}
void downAll() 
{
  for(int dot = 0; dot < NUM_LEDS; dot++)
  {
    leds[dot] = CRGB::Black;
  }
  FastLED.show();
}


