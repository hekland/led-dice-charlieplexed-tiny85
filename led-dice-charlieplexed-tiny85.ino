/* 6-face LED Dice using Charlieplexing on the ATtiny85
* 
* This program implements a 6-faced LED dice with a ball-switch for detecting throwing.
* This runs on an ATtiny85 by using Charlieplexing to control the seven LEDs with only
* four pins, and one pin for the ball switch to detect throwing (via interrupt). 
* The ATtiny85 powers off when done showing the number to save power, avoiding the need 
* for a power switch.
*
* Circuit diagram for the dice:
*
*        +--------+
* PB1 +-+|  470   |+-----+------++--------+--------+
*        +--------+      |      |         |        |
*                       ---   -----       |        |
*                       \1/    /2\        |        |     +-----+
*                      -----   ---        |        |     |1   2|
*        +--------+      |      |         |        |     |     |
* PB0 +-+|  470   |+-----+------+        ---     -----   |3 7 4|
*        +--------+      |      |        \5/      /6\    |     |
*                       ---   -----     -----     ---    |5   6|
*                       \3/    /4\        |        |     +-----+
*                      -----   ---        |        |
*        +--------+      |      |         |        |
* PB4 +-+|  470   |+-----+------+---------+--------+
*        +--------+
*
*
*                                            +----+ PB2
*        +--------+                          |
* PB3 +-+|  470   |+-----------+            |o
*        +--------+           ---         ==|
*                             \7/           |o
*                            -----           |
*                              |             |
* GND +------------------------+-------------+
* 
* Low-power modes are attained using the LowPower library:
* https://github.com/sej7278/LowPower which is based on the 
* LowPower library from Rocket Scream Electronics(www.rocketscream.com)
* 
* Written by: Fredrik Hekland
* Date: 2017-08-22
* 
* This code is licensed under Creative Commons Attribution-ShareAlike 3.0
* Unported License.
*/

//#define SERIAL_DEBUG

#include "LowPower.h"

const uint16_t timeout_ms = 4000; // Show number for 4 seconds

const int8_t IN = -1;
volatile bool isDiceThrown = false;
const int8_t NUMBERS = 6;
const int8_t N_LED_PINS = 4;
const int8_t THROW_PIN = 2;
const int8_t LED_PINS[N_LED_PINS] = {1, 0, 4, 3};
const int8_t LED_PIN_STATES[8][N_LED_PINS] = {{IN,   IN,   IN,   IN},
                                              {IN,   IN,   IN,   HIGH},
                                              {HIGH, LOW,  IN,   IN},
                                              {LOW,  HIGH, IN,   IN},
                                              {IN,   HIGH, LOW,  IN},
                                              {IN,   LOW,  HIGH, IN},
                                              {HIGH, IN,   LOW,  IN},
                                              {LOW,  IN,   HIGH, IN}};

/* Number in a row indicates which entries in LED_PIN_STATES to cycle 
 *  through to form a number of the dice. Zero breaks out of for-loop as remaining pins are already inputs. */
const int8_t DICE_NUMBERS[NUMBERS+1][NUMBERS] = {{0,0,0,0,0,0}, // 0, not used
                                                 {1,0,0,0,0,0}, // 1
                                                 {4,5,0,0,0,0}, // 2
                                                 {1,4,5,0,0,0}, // 3 
                                                 {2,3,6,7,0,0}, // 4 
                                                 {1,2,3,6,7,0}, // 5
                                                 {2,3,4,5,6,7}};// 6 

/**
 * Make a random seed for number generation.
 * Select throw-pin where the ball-switch is connected (pin with external interrupt capability)
 * Enable external interrupt for throwing dice
 */
void setup()
{
  randomSeed(analogRead(0));
  pinMode(THROW_PIN, INPUT_PULLUP);
  turnOffLEDs();
  enableExternalInterrupt();
#ifdef SERIAL_DEBUG
  Serial.begin(9600);
#endif
}

/**
 * Loop goes into power-off when done showing number.
 * External interrupt from throw-switch will wake up processor to show a new number.
 */
void loop() 
{
  if( isDiceThrown )
  {
    disableExternalInterrupt(); // disable INT0 to avoid messing with Charlieplexing
    rollDice();
    isDiceThrown = false;
    enableExternalInterrupt(); // ready for a new throw
  }
  LowPower.powerDown(SLEEP_FOREVER, ADC_OFF, BOD_OFF);
}

/**
 * External pin interrupt is enabled
 */
void enableExternalInterrupt()
{
  GIMSK |= _BV(6);
}

/**
 * External pin interrupt is disabled
 */
void disableExternalInterrupt()
{
  GIMSK &= ~_BV(6);
}

/**
 * Interrupt service routine to indicate a thrown dice.
 */
ISR(INT0_vect)
{
  isDiceThrown = true;
}

/**
 * Roll the dice by drawing a random number and cycle fast through the 
 * LEDs in the number. This is lighting them up sequentially, but does it so fast 
 * that they appear lit up simultaneously.
 */
void rollDice()
{
  uint32_t number = random(NUMBERS)+1;
#ifdef SERIAL_DEBUG
  Serial.println(number);
#endif
  uint32_t start = millis();
  do // Charlieplexing LEDs in rapid succession to paint the dice face correctly
  {
    for(int8_t num2state=0; num2state < NUMBERS; ++num2state)
    {
      int8_t pinStates = DICE_NUMBERS[number][num2state];
      if(pinStates == 0)
        break; // no more LEDs to light up for this dice face
      for(int8_t pinIdx=0; pinIdx < N_LED_PINS; ++pinIdx)
      {
        setPin(LED_PINS[pinIdx], LED_PIN_STATES[pinStates][pinIdx]);
      }
    }
    turnOffLEDs();
  } while( (uint16_t)(millis() - start) < timeout_ms );
  
  turnOffLEDs();
}

/**
 * Set a pin to input, or output with high/low (source/sink current)
 */
void setPin(int8_t pinNr, int8_t pinState)
{
  if( pinState == IN )
  {
    pinMode( pinNr, INPUT);
    digitalWrite( pinNr, LOW);
  }
  else
  {
    pinMode( pinNr, OUTPUT);
    digitalWrite( pinNr, pinState);
  }
}

/**
 * Set all pins to inputs to shut off all LEDs.
 */
void turnOffLEDs()
{
  setPin(LED_PINS[0], IN);
  setPin(LED_PINS[1], IN);
  setPin(LED_PINS[2], IN);
  setPin(LED_PINS[3], IN);
}

