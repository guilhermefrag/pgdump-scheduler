from apscheduler.schedulers.background import BlockingScheduler
from .jobs import database_dump
from tzlocal import get_localzone
from backports import zoneinfo

def start():
    
    #date: use when you want to run the job just once at a certain point of time
    #interval: use when you want to run the job at fixed intervals of time
    #cron: use when you want to run the job periodically at certain time(s) of day
    SP = zoneinfo.ZoneInfo("America/Sao_Paulo")
    scheduler = BlockingScheduler()
    scheduler.add_job(database_dump, "cron",timezone = SP, day_of_week='mon-fri', hour=22, minute= 47) 
    scheduler.start()
    
    