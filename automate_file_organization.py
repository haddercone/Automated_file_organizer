import shutil
import os
os.chdir('C:\\Users\\44rob\\')
source_directory = 'C:\\Users\\44rob\\Downloads\\'
file_formats = {
                '.png': 'C:\\Users\\44rob\\Pictures\\Saved Pictures\\',
                'jpeg': 'C:\\Users\\44rob\\Pictures\\Saved Pictures\\',
                'jpg': 'C:\\Users\\44rob\\Pictures\\Saved Pictures\\',
                '.txt': 'C:\\Users\\44rob\\Documents\\Text_files\\',
                '.gif': 'C:\\Users\\44rob\\Videos\\GIF\\',
                '.exe': 'C:\\Users\\44rob\\Apps(.exe)\\',
                '.pptx': 'C:\\Users\\44rob\\Documents\\Documents\\',
                '.docx': 'C:\\Users\\44rob\\Documents\\Documents\\',
                '.wmv': 'C:\\Users\\44rob\\Videos\\videos\\',
                '.mp3': 'C:\\Users\\44rob\\Music\\',
                '.mp4': 'C:\\Users\\44rob\\Videos\\videos\\',
                }

for file_name in os.listdir('C:\\Users\\44rob\\Downloads'):
    for extension in file_formats:
        if file_name.endswith(extension):
            if os.path.isfile(file_formats[extension] + file_name):
                continue
            else:
                shutil.move(source_directory + file_name, file_formats[extension] + file_name)
        else:
            continue
