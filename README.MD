
**Use this code inside a django project**

1 - To run the scheduler dump:

    $ cd ~/

    $ nano .pgpass

    Insert the following lines inside .pgpass 
    (if you want more than one database connected, just add like bellow)

    host:port:databse:user:psswd
    host2:5432:db2:user:psswd

2 - Config the scheduler

    To configure your command go to dump.jobs.run and create your own command
    To add your def to the scheduler list, go to dump.jobs.run

3- running 

    python3 manage.py runserver
