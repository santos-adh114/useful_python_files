import os,sys
from pymatgen.io.vasp import Poscar


def cif_generator(file_input,file_output):
    poscar = Poscar.from_file(file_input)
    structure = poscar.structure
    structure.to(filename=str(file_output)+".cif")
