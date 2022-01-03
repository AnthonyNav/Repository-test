# We import the packages
import socket
# We define the instructions
# We bring the hostname with a method 
def run():
    # We bring the hostname with a method 
    hostname = socket.gethostname()
    # with the hostname, we bring the ip
    ip = socket.gethostbyname(hostname)
    # Show the information 
    print(f"""
    Your device's name is {hostname}
    And your IP is {ip} 
    """)
    # End of the script
if __name__ == '__main__':
    run()
