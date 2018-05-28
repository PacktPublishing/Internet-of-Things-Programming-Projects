import Adafruit_DHT

dht_sensor = Adafruit_DHT.DHT11
pin = 19
humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, pin)

print(humidity)
print(temperature)
