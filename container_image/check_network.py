import speedtest
from pythonping import ping

print()
print("Ping test: to ec2.us-east-1.amazonaws.com")
ping('ec2.us-east-1.amazonaws.com', interval=1, count=5, verbose=True)
print()

print("Ping test: to ec2.us-west-2.amazonaws.com")
ping('ec2.us-west-2.amazonaws.com', interval=1, count=5, verbose=True)
print()

speed_test = speedtest.Speedtest()
bserver = speed_test.get_best_server()
latency = bserver['latency'] # the latency to the test server
country = bserver['country'] 
location = bserver['name']

#dlspeed = int(speed_test.download() / (1000 * 1000))  # Convert to Mbps, not Mib
#ulspeed = int(speed_test.upload() / (1000 * 1000))  # Convert to Mbps, not Mib

print(f"Country: {country}")
print(f"Location: {location}")
print(f"Latency: {latency} ms")
print()
