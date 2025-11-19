from celery import shared_task
import time

@shared_task
def heavy_task_one():
    time.sleep(10)
    return "Task One Completed!"

@shared_task
def heavy_task_two():
    time.sleep(5)
    return "Task Two Completed!"
@shared_task
def scheduled_task_code():
    print("Running scheduled task from CODE every 3 minutes")
    return "Scheduled OK"
