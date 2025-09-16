# LOLIN SSD1680 for MicroPython

## Intro

This Micropython library is a translation from the Wemos LOLIN_EPD_Library [repo](https://github.com/wemos/LOLIN_EPD_Library).
Translation by Microsoft Copilot on directions and feedback by me, Paulus Schulinck (Github handle: @PaulskPt).

## Hardware used

1) Pimoroni Pico LiPo 2XL W [info](https://shop.pimoroni.com/products/pimoroni-pico-lipo-2-xl-w?variant=55447911006587)
2) Lolin 2.13 inch, 3-Color e-Paper display, 250 x 122 pixels [info](https://www.wemos.cc/en/latest/d1_mini_shield/epd_2_13_3.html);
3) eight jumper wires male-male dupont pins [info](https://shop.pimoroni.com/products/jumper-jerky?variant=304798331)
4) header 8-pin [info](https://shop.pimoroni.com/products/break-away-headers?variant=7351054145).

## Wiring

a. Solder the 8-pin header onto the e-Paper board. 

b. connect the eight jumper wires refered at 3) above to make the connection between the Pico LiPo 2XL W board and the e-Paper display board:

```

For SPI:
+----------+-----+---------+
| Function | Pin | Note    |
+----------+-----+---------+
| sck      |  10 | Clock   |
+----------+-----+---------+
| mosi     |  11 | Data    |
+----------+-----+---------+

For EPD object:
+----------+-----+--------------+
| Function | Pin | Note         |
+----------+-----+--------------+
| cs       |  32 | Chip select  |
+----------+-----+--------------+
| dc       |  35 | Data/Command |
+----------+-----+--------------+
| rst      |  36 | Reset        |
+----------+-----+--------------+
| busy     |  31 | Busy         |
+----------+-----+--------------+

General/Power:
+----------+-----+-----------------+
| Function | Pin | Note            |
+----------+-----+-----------------+
| + (3V3)  |  +  | Supply voltage  |
+----------+-----+-----------------+
| - (GND)  |  -  | Ground          |
+----------+-----+-----------------+

```

## Image: 

[here](https://github.com/PaulskPt/LOLIN_SSD1380_for_MicroPython/blob/main/images/20250914_141003.jpg)

## Example 
[here](https://github.com/PaulskPt/LOLIN_SSD1380_for_MicroPython/blob/main/example/Lolin_EPD_test_by_MS_Copilot_v2.py)

## Notes about the dimensions of this display

On internet I found much confusion about the dimensions of this display.
On the back of my Lolin 2.13 inch e-Paper display is written "250x122" and that are the dimensions I use in this MicroPython example.
The same dimensions I used in an Arduino sketch. 250 x 122 px works OK with the board I use.


