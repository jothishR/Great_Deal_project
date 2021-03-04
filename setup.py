import os
import json
import sys
import subprocess
import logging

installed_pkgs = []
path = os.path.abspath("requirements.json")
###install requirement packages
def get_pkgs():
    #get packages from json
    with open(path) as pkgs:
        lst_pkgs = json.loads(pkgs.read())
    return lst_pkgs

def install_pkgs(package):
    print("pacakges is installing...")
    proc = subprocess.Popen([sys.executable, "-m", "pip", "install", package], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    print(out)
    print(err)


def run_django_server():
    p=os.getcwd()
    """ser_path= p + '\\Great_deal_mart\\manage.py'
    process = subprocess.Popen([sys.executable,ser_path,"runserver"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(stdout)"""
    sys.path.append(p + '\\Great_deal_mart')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Great_deal_mart.settings")
    from django.core.management import execute_from_command_line
    args = ['name', 'runserver', '0.0.0.0:8080']
    execute_from_command_line(args)

def verify_packages():
    lst_pkgs = get_pkgs()
    proc = subprocess.Popen([sys.executable, "-m", "pip", "list"], stdout=subprocess.PIPE)
    out = proc.communicate()
    lines = out[0].decode(encoding="UTF-8").split("\r\n")
    for ind in range(2, len(lines)):
        p=lines[ind].split(" ")[0]
        installed_pkgs.append(p)
    print(installed_pkgs)






verify_packages()
run_django_server()
#a = get_pkgs()
#install_pkgs(a["req_pkges"])






