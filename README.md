# SUNCLOCK

---
<p>I got the idea for this clock when I was looking for a project in which I could experiment with a segment display.</p> 
<p>To make it more interesting I wanted to display the sunrise and sunset too. To do this I looked for a spherical 
neopixel strip. So this clock will show the local time, the sunset and sunrise. Onm top of that I added a oled display 
on which I can
show the temperature and humidity.</p>

---
## WORKINGS
When you connect the device to a power source using the USB connector the clock will start up and try to connect to the internet.
It loops through the connections found in 

---
## PARTS
 
### ELECTRONICS
- 1 [Raspberry pico W](https://www.kiwi-electronics.com/nl/raspberry-pi-pico-w-10938) This microcontroller
is convenient for this project, as it has multiple L2C channels. The wifi is essential for the clock to sync with 
a time api on internet
- 1 [big 7-segment display](https://www.kiwi-electronics.com/nl/3cm-4-digit-7-segment-display-met-i2c-backpack-rood-418)
make sure the display has an i2c pack. Its way easier to control the segments. I do encourage to experiment with bare 
segment displays to discover how shift registers work. I need to look into that when I start working on my nixie tube 
clock ;)
- 2 [Neopixel strips, spherical](https://www.kiwi-electronics.com/nl/neopixel-1-4-60-ring-5050-rgb-led-w-integrated-drivers-2786)
- 1 [OLED display](https://www.bitsandparts.nl/Display-OLED-128x32-0-91-inch-I2C-Blauw-p1067279)
- 1 [DHT22](https://www.kiwi-electronics.com/nl/dht22-am2302-temperatuur-vochtigheidssensor-plus-weerstand-503?search=dht22)
sensor Make sure you use the DHT22 and not the DHT11.
- 1 4K7 resistor

### 3D PRINTS

- 

### LASER CUTTED

---

