import subprocess
from pathlib import Path


def clearFile(cwd):
  with open(cwd + f"case{i}/program_res.txt", "w") as f:
    pass


cwd = "/home/CIN/mvhx/projects/exercicios-IP/lista4/q2/tests/"
cases_folders = Path(cwd)

for i in range(1, list(cases_folders.iterdir()).__len__() + 1):
  clearFile(cwd)

  with (
    open(cwd + f"case{i}/data.txt", "r") as data,
    open(cwd + f"case{i}/program_res.txt", "a") as program_res,
  ):
    subprocess.run(["python3", "/home/CIN/mvhx/projects/exercicios-IP/lista4/q2/idx.py"], stdin=data, stdout=program_res)

  with (
    open(cwd + f"case{i}/program_res.txt", "r") as program_res,
  ):
    content = program_res.read()
    content = content.rstrip()
  clearFile(cwd)

  with (
    open(cwd + f"case{i}/program_res.txt", "w") as program_res,
  ):
    program_res.write(content)

  with (
    open(cwd + f"case{i}/case_output.txt", "r") as case_output,
    open(cwd + f"case{i}/program_res.txt", "r") as program_res,
  ):
    if program_res.read() == case_output.read():
      print(f"✅ case{i}")
    else:
      print(f"❌ case{i}")
