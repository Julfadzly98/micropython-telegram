from machine import Pin, time_pulse_us
import time

# Pin configuration
TRIG_PIN = 13  # GPIO13
ECHO_PIN = 12  # GPIO12

# Initialize pins
trig = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)

def measure_distance():
    # Send a 10us pulse to trigger pin
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    # Measure the duration of the echo pulse
    try:
        pulse_duration = time_pulse_us(echo, 1, 30000)  # Timeout: 30ms (30000us)
    except OSError:
        return None  # Return None if no echo is detected (timeout)

    # Calculate distance in cm (speed of sound = 34300 cm/s)
    distance = (pulse_duration / 2) * 0.0343
    return distance

while True:
    distance = measure_distance()
    if distance is not None:
        print("Distance: {:.2f} cm".format(distance))
    else:
        print("Out of range or no echo detected.")
    
    time.sleep(1)  # Delay between measurements
