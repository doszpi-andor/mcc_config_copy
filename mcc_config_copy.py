from os.path import split, isfile
from pathlib import Path
from shutil import copy
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.messagebox import showerror, showinfo, showwarning


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


def read_mplab_default_path():
    try:
        mplab_properties = str(Path.home()) + '\\AppData\\Roaming\\mplab_ide\\dev\\v6.00\\config\\Preferences.properties'

        with open(mplab_properties, 'r', encoding='utf-8') as read_file:
            lines = [line for line in read_file]
        for line in lines:
            if line[0:22] == 'MPLAB_PROJECTS_FOLDER=':
                return str(line[22:-1])
    except FileNotFoundError:
        return '.'

    return '.'


def read_mplab_project_path():
    project = askdirectory(initialdir=read_mplab_default_path())

    if project != '' and project[-1] == 'X':
        return project
    else:
        raise OpenMplabProjectException


def mplab_project_name(mplab_project_path):
    if mplab_project_path != '' and mplab_project_path[-1] == 'X':
        project_folder = str(split(mplab_project_path)[-1])
        project_name = str(project_folder[:-2])
        return project_name
    else:
        raise OpenMplabProjectException


def is_mcc_file_in_project(mplab_project_path):
    if isfile(mplab_project_path + '/' + mplab_project_name(mplab_project_path) + '.mc3'):
        return True
    else:
        return False


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

    if is_mcc_file_in_project(mplab_project):
        copy(mcc_file, mplab_project + '/' + mplab_project_name(mplab_project) + '.mc3')
        showinfo('OK', 'MCC file copy ready')
    else:
        showwarning('Error', 'Running MCC first!')
