import random

def generate_mac_address():
    # Generate a random MAC address
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    # Format the MAC address as a string
    return ':'.join(['{:02x}'.format(x) for x in mac])

# Generate a random MAC address and print it
print(generate_mac_address())
