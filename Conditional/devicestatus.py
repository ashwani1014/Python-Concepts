device_status="active"
temprature=20

if device_status=="active":
    if temprature>30:
        print("High Temprature Alert")
    else:
        print("Temp is normal")
else:   
    print("Device is Offline")         