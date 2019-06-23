#include <Arduino.h>
#include <main.h>

#define NUM_LEDS 8
#define DATA_PIN PB13 
#define CLOCK_PIN PB12

RGB leds[NUM_LEDS];

void setup()
{
  pinMode(CLOCK_PIN, OUTPUT);
  pinMode(DATA_PIN, OUTPUT);
  clear();
}
void loop()
{
  for(int i=0;i<NUM_LEDS;i++)
  { 
    leds[i].r=random(0,255);
    leds[i].g=random(0,255);
    leds[i].b=random(0,255);
  }
  show();
  clear();
  show();
  delay(100);
}
void show()
{
  for(int i=0;i<NUM_LEDS;i++)
  {
    shiftOut(DATA_PIN, CLOCK_PIN, MSBFIRST, leds[i].r);
    shiftOut(DATA_PIN, CLOCK_PIN, MSBFIRST, leds[i].g);
    shiftOut(DATA_PIN, CLOCK_PIN, MSBFIRST, leds[i].b);
  }
}
void clear(){
  for (int i=0;i<NUM_LEDS;i++)
  {
    leds[i].r=0;
    leds[i].g=0;
    leds[i].b=0;
  }
}