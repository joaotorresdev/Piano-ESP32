import machine #informações (biblioteca) sobre o ESP32
import time

led = machine.Pin(14, machine.Pin.OUT)
led2 = machine.Pin(13, machine.Pin.OUT)
led3 = machine.Pin(12, machine.Pin.OUT)
cont = 1


while (cont <= 10):
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
   
    led2.on()
    time.sleep(0.5)
    led2.off()
    time.sleep(0.5)

    led3.on()
    time.sleep(0.5)
    led3.off()
    time.sleep(0.5)
    cont = cont + 1

