import http_requests
import web_scraper
import speech_to_text
import text_to_speech
import pi_gui
import file_text_reader

# create a common root
# import pi_momentory_button
import pen_drive_files_list
import display_list

# # get this footed files
# supported_files=pen_drive_files_list.get_list("F:/")
# print("supported_files hola")
# # display the list of files in the USB drive
# display_list.display(supported_files)


usb_name = "F:/"
# get this footed files
supported_files = pen_drive_files_list.get_list(usb_name)
context_options = ["USB Drive", "Website's URL"]

# display the list of files in the USB drive
display_list.display(context_options)

selected_method = display_list.item_selected

# print(selected_method)
if "USB" in selected_method:

    # Website URL
    # else:
