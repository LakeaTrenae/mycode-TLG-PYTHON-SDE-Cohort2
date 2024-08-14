#!/usr/bin/env python3


import shutil
import os


os.chdir('/home/student/mycode/')


shutil.move('raynor.obj', 'ceph_storage/')


xname = input('What is the new name for kerrigan.obj? ')



shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)



def main():
    """
    Main function to perform file operations.
    - Change the working directory to ~/mycode/
    - Move the raynor.obj file to the ceph_storage/ directory
    - Prompt user for a new name for the kerrigan.obj file
    - Rename kerrigan.obj with the new name provided by the user
    """
    # Change the working directory to ~/mycode/
    os.chdir('/home/student/mycode/')

    # Move the raynor.obj file to the ceph_storage/ directory
    shutil.move('raynor.obj', 'ceph_storage/')

    # Prompt the user for a new name for the kerrigan.obj file
    new_name = input('What is the new name for kerrigan.obj? ')

    # Rename kerrigan.obj with the new name provided by the user
    shutil.move('ceph_storage/kerrigan.obj', f'ceph_storage/{new_name}')

if __name__ == "__main__":
    main()
