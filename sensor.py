from sense_hat import SenseHat #import SenseHat packages
import database
import webex

sense = SenseHat()  #establish connection to hat

temp_threshold = 120

# Get temperature and print to console
temp = sense.get_temperature()
# print("Temperature in C = " +str(temp))


# Get temperature and print to console
tempF = temp *(9/5) + 32
intTempF = int(tempF)
# print("Temperature in F = " +str(intTempF))



# Get pressure and print to console
# pressure = sense.get_pressure()
# print("Pressure = " +str(pressure))


# Get humidity and print to console
humidity = sense.get_humidity()
intHumidity = int(humidity)
# print("Humidity = " +str(intHumidity))

database.init()

database.add_new(intTempF, intHumidity)

database.read_table()

if (tempF > temp_threshold): 
    webex.webex_alert("IT IS HOT")



