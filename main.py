import network
import urequests
import time
from machine import Pin, ADC

# =====================
# WIFI CONFIG
# =====================
SSID = "NAMA_WIFI"
PASSWORD = "PASSWORD_WIFI"

SERVER_URL = "http://IP_KOMPUTER_KAMU:5000"

# =====================
# PIN CONFIG
# =====================
pir = Pin(14, Pin.IN)
relay = Pin(26, Pin.OUT)

ldr = ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)

# =====================
# WIFI CONNECT
# =====================
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

print("Connecting WiFi...")
while not wifi.isconnected():
    time.sleep(1)

print("WiFi Connected:", wifi.ifconfig())

# =====================
# MAIN LOOP
# =====================
while True:
    try:
        pir_value = pir.value()
        ldr_value = ldr.read()

        # Ambil perintah dari server
        r = urequests.get(SERVER_URL + "/api/control")
        control = r.json()
        r.close()

        mode = control["mode"]
        lamp_cmd = control["lamp"]

        # Logika AUTO
        if mode == "AUTO":
            if ldr_value < 500 or pir_value == 1:
                relay.value(1)
                lamp_status = "ON"
            else:
                relay.value(0)
                lamp_status = "OFF"

        # Logika MANUAL
        else:
            if lamp_cmd == "ON":
                relay.value(1)
                lamp_status = "ON"
            else:
                relay.value(0)
                lamp_status = "OFF"

        # Kirim data sensor ke server
        data = {
            "pir": pir_value,
            "ldr": ldr_value,
            "lamp": lamp_status
        }

        urequests.post(SERVER_URL + "/api/sensor", json=data).close()

        print(data)
        time.sleep(2)

    except Exception as e:
        print("Error:", e)
        time.sleep(5)
