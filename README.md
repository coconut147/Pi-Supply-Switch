# Pi-Supply-Switch

This is a fork of the original Pi Supply Switch project by PiSupply.

This branch is used on my RetroPi installation.


Pi Supply Switch On/Off Switch for Raspberry Pi - https://www.pi-supply.com/product/pi-supply-raspberry-pi-power-switch/



#Installation
1. Login via SSH or via the console.
2. Run the following command and Pi Switch will be setup and installed: 
```bash
curl -sSL https://pisupp.ly/piswitchcode | sudo bash
```

With this new script any standard pin can be chosen to provide the function previusly covered by pins 7 and 8.
Within softshut.py you can change the assignement which by default is

```python
PinSeven = 7
PinEight = 11
```

This means that pin 7 coming from the Pi Switch goes to pin 7 on the Raspberry Pi and that pin 8 from the Pi Switch goes to pin 11 on the Raspberry Pi.

```
PiSwitch 7 <---> RPi 7
PiSwitch 8 <---> RPi 11
```

Rememeber that the notation used is the physical notation only.
