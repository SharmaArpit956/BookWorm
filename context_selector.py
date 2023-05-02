import http_requests
import web_scraper
import speech_to_text
import text_to_speech
import pi_gui
import file_text_reader
import context_selection_url
import context_selection_pdf

# create a common root
# import pi_momentory_button
import pen_drive_files_list
import display_list


def context_selection():
    usb_name = "F:/"
    # get this footed files
    supported_files = pen_drive_files_list.get_list(usb_name)
    context_options = ["USB Drive", "Website's URL"]

    # display the list of files in the USB drive
    display_list.display(context_options)

    selected_method = display_list.item_selected

    # print(selected_method)
    if "USB" in selected_method:
        # # get this footed files
        # supported_files = pen_drive_files_list.get_list(usb_name)
        # print("supported_files")
        # # display the list of files in the USB drive
        # display_list.display(supported_files)
        # context=context_selection_pdf.context
        context = context_selection_pdf.doc_reader(usb_name)
        
    # Website URL
    else:
        context_selection_url.display()
        context = context_selection_url.url

    # print(context)
    return context
