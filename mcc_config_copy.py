from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.messagebox import showerror


def read_mcc_file_path():
    mcc_file = askopenfilename(filetypes=[("MCC file", "*.mc3")], initialdir='.')

    if mcc_file.split('.')[-1] != 'mc3':
        raise FileExistsError

    return mcc_file


def read_mplab_project_path():
    project = askdirectory()

    if project != '' and project[-1] == 'X':
        return project
    else:
        raise 
