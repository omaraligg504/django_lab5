from django.http import JsonResponse
from .tasks import heavy_task_one, heavy_task_two

def run_tasks(request):
    task1 = heavy_task_one.delay()
    task2 = heavy_task_two.delay()

    return JsonResponse({
        "task1_id": task1.id,
        "task2_id": task2.id,
        "message": "Tasks have started in the background!"
    })
