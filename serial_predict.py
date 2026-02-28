import serial

ser = serial.Serial('COM4', 921600, timeout=1)

while True:
    data = ser.read(100)
    if data:
        print("Received:", len(data))
