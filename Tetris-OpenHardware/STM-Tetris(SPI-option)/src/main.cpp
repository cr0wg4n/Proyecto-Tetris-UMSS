#include <Arduino.h>
#include <main.h>
#include <SPI.h>

#define NUM_LEDS 6

//DATA_PIN PB15, CLOCK_PIN PB13
SPIClass SPI_2(2);
RGB leds[NUM_LEDS];
void setup()
{
  SPI_2.begin();
  SPI_2.setBitOrder(MSBFIRST);
  SPI_2.setDataMode(SPI_MODE0); 
  SPI_2.setClockDivider(SPI_CLOCK_DIV4);	
}
void clear(){
  for (int i = 0; i < NUM_LEDS; i++ ) {
    leds[i].r=0;
    leds[i].g=0;
    leds[i].b=0;
  }
  show();
}
void show(){
  for (int i = 0; i < NUM_LEDS; i++ ) {
    SPI_2.transfer( leds[i].r );
    SPI_2.transfer( leds[i].g );
    SPI_2.transfer( leds[i].b );
  }
  delay(1);
}
void loop() 
{
  for (int i = 0; i < NUM_LEDS; i++ ) {
    leds[i].r=random(0,255);
    leds[i].g=random(0,255);
    leds[i].b=random(0,255);
  }
  show();
  delay(2000); 
}