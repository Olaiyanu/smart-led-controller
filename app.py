from flask import Flask, render_template, redirect
import serial
import time
import serial.tools.list_ports

app = Flask(__name__)

try:
    # Attempt to connect to the Arduino
    arduino = serial.Serial('COM3', 9600)
    time.sleep(2)
except serial.SerialException:
    print("Warning: Could not connect to Arduino on COM3.")
    print("Please check your connection or update the COM port. Available ports are:")
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(f" - {port.device}: {port.description}")
    print("Running without serial.")
    arduino = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/led1/on')
def led1_on():
    if arduino:
        arduino.write(b'A')
    return redirect('/')

@app.route('/led1/off')
def led1_off():
    if arduino:
        arduino.write(b'a')
    return redirect('/')

@app.route('/led2/on')
def led2_on():
    if arduino:
        arduino.write(b'B')
    return redirect('/')

@app.route('/led2/off')
def led2_off():
    if arduino:
        arduino.write(b'b')
    return redirect('/')

@app.route('/led3/on')
def led3_on():
    if arduino:
        arduino.write(b'C')
    return redirect('/')

@app.route('/led3/off')
def led3_off():
    if arduino:
        arduino.write(b'c')
    return redirect('/')

if __name__ == '__main__':
    # host='0.0.0.0' makes the server accessible from your phone on the same Wi-Fi
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False, ssl_context='adhoc')