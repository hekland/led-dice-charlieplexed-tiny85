# README #

### What is this repository for? ###

**6-sided LED Dice using Charlieplexing on the ATtiny85**

* Version 1.0 (2017-08-22): Initial release

This program implements a 6-faced LED dice with a ball-switch for detecting throwing.
This runs on an ATtiny85 by using Charlieplexing to control the seven LEDs with only
four pins, and one pin for the ball switch to detect throwing (via external interrupt). 
The ATtiny85 powers off when done showing the number to save power, avoiding the need 
for a power switch.

The ATtiny85 is using a 1MHz internal clock. It's using ~2mA when showing the numbers,
and 160nA when powered off. Running on a standard CR2032 button cell with 220mAh, 
this should provide over 130000 throws (110 hours of fun with 3 sec on-time per throw). 
Or you can put it in the drawer and the battery will last for 157 years in power-off mode.
(way longer than the shelf-life of the battery).

Low-power modes are attained using the LowPower library:
https://github.com/sej7278/LowPower which is based on the 
LowPower library from Rocket Scream Electronics (www.rocketscream.com)

Disclaimer: No checks have been done on the distribution of the random number generator
of this dice. It may be a loaded dice.

### How do I get set up? ###

**What you need**

* [ATtiny support for Arduino IDE](https://github.com/damellis/attiny)
* [Low-power Library for Arduino with ATtiny85-support](https://github.com/sej7278/LowPower)
* An Arduino Uno for programming the ATtiny85.
* Some hardware as described in the Fritzing file.

**How to program the ATtiny85**

* [Setup your Uno as programmer](http://highlowtech.org/?p=1706)
* [Burn bootloader on the ATtiny85 using the 1MHz internal clock, and install sketch](http://highlowtech.org/?p=1695)

### Contribution guidelines ###


### Who do I talk to? ###

Written by: Fredrik Hekland
