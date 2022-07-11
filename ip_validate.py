# importing necessary packages
import ipaddress

# inputing data
ip_addr = input("please enter an ip address : ")
try:
    # checking to see if the insterted value is 
    # actually an ip address        
    ip = ipaddress.ip_address(ip_addr)
    print(ip_addr, "is a valid IPV", ip.version, "address")
except Exception as e:
    # if the value is not an ip adress then 
    # the method will throw an error
    print(e)
    print("invalid ip address")