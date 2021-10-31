# -*- coding:UTF-8 -*-

import RPi.GPIO as GPIO
import time

#Definition of RGB module pin
LED_R = 22
LED_G = 27
LED_B = 24

#Set the GPIO port to BCM encoding mode.
GPIO.setmode(GPIO.BCM)

#Ignore warning information
GPIO.setwarnings(False)

#RGB pins are initialized into output mode
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)
pwm_rled = GPIO.PWM(LED_R, 1000)
pwm_gled = GPIO.PWM(LED_G, 1000)
pwm_bled = GPIO.PWM(LED_B, 1000)
pwm_rled.start(0)
pwm_gled.start(0)
pwm_bled.start(0)

def color_led_pwm(iRed,iGreen, iBlue):
    v_red = (100*iRed)/255
    v_green = (100*iGreen)/255
    v_blue = (100*iBlue)/255
    pwm_rled.ChangeDutyCycle(v_red)
    pwm_gled.ChangeDutyCycle(v_green)
    pwm_bled.ChangeDutyCycle(v_blue)
    time.sleep(0.02)
	

def color_led_off(delay):
    pwm_rled.ChangeDutyCycle(0)
    pwm_gled.ChangeDutyCycle(0)
    pwm_bled.ChangeDutyCycle(0)
    time.sleep(delay)
	
    
# A red, D yellow, Y green, E turquose, N blue 

#Display 7 color LED
try:
    
    # A red
    color_led_pwm(255,0,0)
    time.sleep(1)
    color_led_off(0.2)
    # D yellow
    color_led_pwm(255,255,0)
    time.sleep(1)
    color_led_off(0.2)
    # Y green
    color_led_pwm(0,255,0)
    time.sleep(1)
    color_led_off(0.2)
    # E turquose
    color_led_pwm(64,224,208)
    time.sleep(1)
    color_led_off(0.2)
    #  N blue 
    color_led_pwm(0,0,255)
    time.sleep(1)
    color_led_off(0.2)

except KeyboardInterrupt:
    print "done"
GPIO.cleanup()
