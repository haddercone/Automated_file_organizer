import shutil
import os
os.chdir('your directory in which your source folder is present')
source_directory = 'Location of your source folder where your files are present'
file_formats = {
                '.png': 'Your folder location where you want to locate your .png files',
                '.txt': 'Your folder location where you want to locate your .txt files',
                '.gif': 'Your folder location where you want to locate your .gif files',
                '.exe': 'Your folder location where you want to locate your .exe files',
                '.pptx': 'Your folder location where you want to locate your .pptx files,
                '.docx': 'Your folder location where you want to locate your .docx files',
                '.wmv': 'Your folder location where you want to locate your .wmv files\',
                '.mp3': 'Your folder location where you want to locate your .mp3 files',
                '.mp4': 'Your folder location where you want to locate your .mp4 files',
  
#   You can add more file extensions and their locations. 
#   Make sure that the location in which you're storing the files should exist.
                }

for file_name in os.listdir(source_directory):
    for extension in file_formats:
        if file_name.endswith(extension):
            if os.path.isfile(file_formats[extension] + file_name):
                continue # remove this if you want to apply the deletion operation 
#                 os.remove(file_name)  # this line permanently deletes the file from the source folder,
                                      # if a copy of that file is present in the destination folder
            else:
                shutil.move(source_directory + file_name, file_formats[extension] + file_name)
        else:
            continue
