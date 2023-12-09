from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror


def read_mcc_file_path():
    mcc_file = askopenfilename(filetypes=[("MCC file", "*.mc3")], initialdir='.')

    if mcc_file.split('.')[-1] != 'mc3':
        showerror('Error', 'File is not MCC file')
        raise FileExistsError

    return mcc_file

