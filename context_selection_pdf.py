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

# pdf_text = ""
# usb_name="K:/"


def doc_reader(usb_name):
    # get this footed files
    supported_files = pen_drive_files_list.get_list(usb_name)

    # display the list of files in the USB drive
    display_list.display(supported_files)

    selected_file = display_list.item_selected
    # print(selected_file)
    file_path = usb_name + selected_file
    pdf_text = file_text_reader.get_text_from_PDF(file_path)
    return pdf_text
    # print(pdf_text)
