"""
    Translation from Arduino to MicroPython by MS Copilot
    Adapted for Pimoroni Pico LiPo 2XL W board
    by Paulus Schulinck (Github handle: @PaulskPt)
    Date: 2025-09-14
    IDE: Thonny
    Using LOLIN_SSD1680 library, part of the Arduino LOLIN_EPD library, translated to MicroPython by MS Copilot
    on directions and feedback by @PaulskPt.
    This MicroPython script has been adapted for Pimoroni Pico LiPo 2XL W by @PaulskPt)
    Version: 2
"""
from machine import Pin, SPI
import time
import framebuf
from lib.LOLIN_SSD1680 import SSD1680, EPD_BLACK, EPD_WHITE, EPD_RED
from lib.fonts import asc2_0806

# Additions by @PaulskPt
# Pins for the Pimoroni Pico LiPo 2XL W:

# --- SPI and Pin Setup ---
spi = SPI(1, baudrate=2_000_000, phase=0, polarity=0, sck=Pin(10), mosi=Pin(11), miso=Pin(12))

cs_pin   = Pin(32, Pin.OUT)   # Chip Select
dc_pin   = Pin(35, Pin.OUT)   # Data/Command
rst_pin  = Pin(36, Pin.OUT)   # Reset
busy_pin = Pin(31, Pin.IN)    # Busy

# --- Display Dimensions ---
WIDTH  = 250
HEIGHT = 122

# --- Initialize Display ---
epd = SSD1680(WIDTH, HEIGHT, spi, dc_pin, rst_pin, cs_pin, busy_pin)

# --- Begin Communication ---
epd.begin(reset=True)

orientation = 180
epd.set_rotation(orientation)  # Landscape mode. Or 0, 90, 270 depending on your desired orientation

def draw_char_scaled(epd, x, y, char, color, scale=1):
    index = ord(char)
    if index < 32 or index > 126:
        index = 32  # fallback to space
    glyph = asc2_0806[index - 32]
    for col in range(6):
        byte = glyph[col]
        for row in range(8):
            if byte & (1 << row):
                px = x + col * scale
                py = y + row * scale
                for dx in range(scale):
                    for dy in range(scale):
                        epd.draw_pixel(px + dx, py + dy, color)

def draw_text(epd, x, y, text, color):
    for i, c in enumerate(text):
        draw_char(epd, x + i * 6, y, c, color)

def draw_text_scaled(epd, x, y, text, color, scale=1):
    for i, c in enumerate(text):
        draw_char_scaled(epd, x + i * 6 * scale, y, c, color, scale)

epd.clear_buffer()
# epd.display()
time.sleep_ms(100)
epd.display()  # Evt. second pass helps eliminate ghosting

# --- Clear Buffers to White Background ---
for i in range(len(epd._buffer_bw)):
    epd._buffer_bw[i] = 0xFF  # White
for i in range(len(epd._buffer_red)):
    epd._buffer_red[i] = 0x00  # No red yet

# --- Create FrameBuffer for Red Text ---
if orientation == 0 or orientation == 180:
    fb_red = framebuf.FrameBuffer(epd._buffer_red, WIDTH, HEIGHT, framebuf.MONO_HLSB)  # Portrait orientation
elif orientation == 90 or orientation == 270:
    fb_red = framebuf.FrameBuffer(epd._buffer_red, WIDTH, HEIGHT, framebuf.MONO_VLSB) # Landscape orientation

# --- Draw Red Text ---

draw_text_scaled(epd, 20, 20, "Pimoroni", EPD_RED, scale=2);
draw_text_scaled(epd, 20, 40, "Pico LiPo 2XL W", EPD_RED, scale=2);
draw_text_scaled(epd, 20, 60, "+ Lolin 2.13 ePD", EPD_RED, scale=2);
draw_text_scaled(epd, 20, 80, "TEST", EPD_RED, scale=2);

# --- Push to Display ---
epd.display()

