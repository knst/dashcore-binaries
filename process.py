#!/usr/bin/env python3
import os

version = input('Version: ')
signed_binaries = input('Seperate unsigned binaries? y/n ') == 'y'
print(signed_binaries)
os.chdir(version)

if not os.path.exists('debug'):
    os.mkdir('debug')
if not os.path.exists('unsigned') and signed_binaries:
    os.mkdir('unsigned')

os.system('mv *debug* debug')
if signed_binaries:
    os.system('mv *unsigned* unsigned')


def process_directory(directory):
    if directory:
        os.chdir(directory)
    os.system('sha256sum * > SHA256SUMS')
    for f in os.listdir('.'):
        if f.startswith('dashcore-'):
            os.system(f"gpg --detach-sign --armour {f}")
    os.system('gpg --clear-sign SHA256SUMS')
    os.remove('SHA256SUMS')
    if directory is not None:
        os.chdir('..')


process_directory(None)  # Processes the current dir
process_directory('debug')
if signed_binaries:
    process_directory('unsigned')

os.chdir('..')
abs_path = os.path.abspath(os.getcwd())
print(os.listdir())
os.chdir('dashpaydash')
print(os.listdir())
os.system(f'gh release create --draft v{version} {"-p" if not signed_binaries else ""} {abs_path}/{version}/dashcore-* {abs_path}/{version}/SHA*')
os.chdir('..')
