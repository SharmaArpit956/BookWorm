import configparser
import os

# Creating a ConfigParser object
config = configparser.ConfigParser()

# VARIBLES RENAME IN FUTURE
# context
# wifi_name
# wifi_password
# Writing to config file

def write_settings(context, wifi_name, wifi_password):

    with open('context.txt', 'w') as f:
        f.write(context)

    config['settings'] = {'wifi_name': wifi_name, 'wifi_password': wifi_password}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


# Reading from config file
def read_settings():
    context, wifi_name, wifi_password = "null", "null", "null"
    
    if os.path.exists('context.txt'):
        with open('context.txt', 'r') as f:
            context= f.read()
   
    config.read('config.ini')
    wifi_name = config['settings']['wifi_name']
    wifi_password = config['settings']['wifi_password']
    print(
        f"context: {context} \nwifi_name: {wifi_name} \nwifi_password: {wifi_password}")
    return context, wifi_name, wifi_password

# if __name__ == "__main__":
#     context, wifi_name, wifi_password = read_settings()
#     print(context)
#     write_settings("null", "null", "null")
