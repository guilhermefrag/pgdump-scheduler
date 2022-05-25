from subprocess import Popen, PIPE

def database_dump():
    print("Inicio")
    dump = f'pg_dump -h localhost -U postgres -p 5432 -d db  > db.sql'
    p = Popen(dump,shell=True,stdin=PIPE,stdout=PIPE,stderr=PIPE)
    