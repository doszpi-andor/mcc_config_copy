from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.messagebox import showerror


class OpenMccFileException(Exception):
    """
    It is not mcc file
    """
    pass


class OpenMplabProjectException(Exception):
    """
    It is not mplab project folder
    """
    pass


def read_mcc_file_path():
    mcc_file = askopenfilename(filetypes=[("MCC file", "*.mc3")], initialdir='.')

    if mcc_file.split('.')[-1] == 'mc3':
        return mcc_file
    else:
        raise OpenMccFileException


def read_mplab_project_path():
    project = askdirectory()

    if project != '' and project[-1] == 'X':
        return project
    else:
        raise OpenMplabProjectException


if __name__ == '__main__':
    try:
        mcc_file = read_mcc_file_path()
    except OpenMccFileException:
        showerror('Error', 'File is not MCC file')
        quit()

    try:
        mplab_project = read_mplab_project_path()
    except OpenMplabProjectException:
        showerror('Error', 'Folder is not MPLAB X Project')
        quit()
