import os
def rename_files():
    file_list = os.listdir(r"C:\Users\hpenvy15\prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory"+saved_path)
    os.chdir(r"C:\Users\hpenvy15\prank")

    for file_name in file_list:
        table = str.maketrans(dict.fromkeys('0123456789'))
        os.rename(file_name, file_name.translate(table))
    os.chdir(saved_path)

rename_files()
