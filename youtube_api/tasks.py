from celery import shared_task




@shared_task
def add(x,y):
    return x + y

@shared_task
def periodic_task():
    print("Hey there the scheduled task has been executed")