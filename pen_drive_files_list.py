import os


# Specify the path to your pen drive
# pen_drive_path = "K:/"
def get_list(pen_drive_path):
    #  Make a list offile extensions do I trade for fromin the if statement later #TODO
    supported_file_extensions = [".pdf",".txt",".doc",".docx"]
    supported_files=[]
    # Loop through the pen drive directory and its subdirectories
    for root, dirs, files in os.walk(pen_drive_path):
        for file in files:
            for supported_file_extension in supported_file_extensions:
                # Check if the file is a text file by its extension
                if file.endswith(supported_file_extension):
                    ## Print the path to the text file
                    # print(os.path.join(root, file))
                    # print(file)
                    supported_files.append(file)
    return supported_files

if __name__ == "__main__":
    print(get_list("K:/"))
