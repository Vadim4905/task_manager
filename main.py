import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_manager.settings")
django.setup()

from home.models import User, Task

task1= Task(
    name= 'do homework',
    description='very important',
    status='put_off',
    )
task1.save()

user1 = User(
    name='vadym',
    email='sefsf@gmail.com',
    role='user'
) 
user1.save()

task = Task.objects.get(id=2)
user = User.objects.get(id=1)

task.user= user
task.status= 'process'
task.save()