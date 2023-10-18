import subprocess

a = subprocess.run('python3 /home/marat/PycharmProjects/polyakov/subproc/sub.py',
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                   encoding='utf-8',
                   shell=True)
st=a.stdout
er=a.stderr
print('st: ', st)
print('er: ', er)
