import urequests  # Module for HTTP requests in MicroPython
import time       # Module for sleep


import network

ssid = "ApaKauMahu?"
password = "smartspace09"

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while not station.isconnected():
    time.sleep(1)
    print("Connecting to WiFi...")

print("Connected to WiFi:", station.ifconfig())



while True:
    time.sleep(1)  # Pause for 1 second
    
    x = "hello"  # Your variable
    
    # Format the URL to include the variable 'x' in the message text
    form_url = "https://api.telegram.org/bot7637161166:AAG6l_5E3UQW_IB2-Yx7tScCowsTm07DIdg/sendMessage?chat_id=187740907&text={}".format(x)
    
    try:
        response = urequests.get(form_url)  # Send the GET request
        print("Message sent successfully:", response.text)
        response.close()  # Close the response to free resources
    except Exception as e:
        print("Error:", e)  # Print any errors that occur


