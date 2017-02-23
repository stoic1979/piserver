#
# main script for starting server
#

from flask import Flask, render_template, request
from nw import *
from bt import *
from gpio import GpioManager

app = Flask(__name__)

gm = GpioManager()

@app.route("/")
def hello():
    templateData = { 'title' : 'Home', 'wifis' : get_wifis() }

    # pass the template data into the template index.html and
    # return it to the user
    return render_template('index.html', **templateData)

@app.route("/wifi")
def wifi():
    templateData = { 'wifis' : get_wifis() }

    return render_template('wifi.html', **templateData)

@app.route("/bluetooth")
def bluetooth():
    templateData = { 'bluetooths' : get_bluetooth_devices() }

    return render_template('bluetooth.html', **templateData)

@app.route("/gpio")
def gpio():
    try:
        pin = request.args.get('pin')

        gm.set_pin_output(int(pin))
        gm.blink_pin(int(pin))

        print "pin:", pin
    except Exception as exp:
        return "GPIO: error -> %s" % exp

    return "gpio success on pin: %s" % str(pin)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
