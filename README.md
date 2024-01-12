# SUNCLOCK

---
<p>I got the idea for this clock when I was looking for a project in which I could experiment with a segment display.</p> 
<p>To make it more interesting I wanted to display the sunrise and sunset too. To do this I looked for a spherical 
neopixel strip. So this clock will show the local time, the sunset and sunrise. Onm top of that I added a oled display 
on which I can
show the temperature and humidity.</p>

---
## WORKINGS

### 1. WIFI
When you connect the device to a power source using the USB connector the clock will start up and try to connect to the internet.
It loops through the connections found in secrets.json (not included in github, because, you know, secret?)
the structure of this json file:
```json
{
  "secrets": [
    {
      "ssid": "acme_guest_wifi",
      "password": "something something something darkside"
    }
  ],
  "time_out": 5,
  "max_tries": 3
}
```
- <b>ssid:</b> your wifi SSID
- <b>password:</b> the password for the SSID
- <b>time_out:</b> time to wait for a connection to be established
- <b>max_tries:</b> number of times to try the wifi connection

The clock will show on the oled display the SSID that it is trying to connect to.
When a connection succeeded, the clock will show the WIFI symbol on the right of the oled display
### 2. GET RTC time
As a WIFI connection is established, the clock will try to get the current local time using worldtimeapi.org.
The settings for this part can be found in [settings.json](./settings.json):
```json
"rtc_url": "http://worldtimeapi.org/api/timezone/Europe/Amsterdam"
```
Make sure you use a timezone for your local time as micropython has no option to calculate UTC to local time. See 
[WorldTimeAPI](https://worldtimeapi.org/pages/examples) for more information.

### 3. GET SUNRISE & SUNSET
Next the clock will get the current sunrise and sunset times. The clock will invoke the api when it has no valid sunset or a sunset from the previous day or older.  
Getting the sunrise and sunset times the clock uses an api from [sunrise-sunset.org](https://sunrise-sunset.org/api).
You can find the settings in [settings.json](./settings.json).
```json
"sunrise_sunset_api": {
    "url": "https://api.sunrise-sunset.org/json",
    "params": {
      "lat": "51.69064188879774",
      "lng": "5.295865449574199",
      "date": "today",
      "formatted": "0",
      "tzId": "Europe/Amsterdam"
    }
  }
```
- <b>url:</b> the URL of the API
- <b>lat (float):</b> Latitude in decimal degrees. Required.
- <b>lng (float):</b> Longitude in decimal degrees. Required.
- <b>date (string):</b> Date in YYYY-MM-DD format. Also accepts other date formats and even relative date formats. 
- <b>formatted (integer):</b> 0 or 1 (1 is default). Time values in response will be expressed following ISO 8601 and day_length will be expressed in seconds. Optional.
- <b>tzid (string):</b> A timezone identifier, like for example: UTC, Africa/Lagos, Asia/Hong_Kong, or Europe/Lisbon. The list of valid identifiers is available in this List of Supported Timezones. Required as micropython cannot calculate UTC to local time.

### 4. SHOW TIME ON SEGMENT DISPLAY

### 5. SHOW SUN ON NEOPIXEL

### 6. SHOW TEMPERATURE ON OLED DISPLAY

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
## BUILDING THE CLOCK


