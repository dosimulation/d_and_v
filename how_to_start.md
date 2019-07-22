## Writing Our first Django App with a Database ##

I have followed [this tutorial](https://docs.djangoproject.com/en/2.2/intro/tutorial01/), it is extremely helpful. 

## Step 1 ##

Once you have confirmed that you have django 2.2 installed on your machine, issue the following
in the current directory: 


```
$ django-admin startproject abbott
```

This will be what we see from the command line. 

    D:\work\abbott\d_and_v>ls
    README.md        how_to_start.md

    D:\work\abbott\d_and_v>django-admin startproject abbott
    D:\work\abbott\d_and_v>ls
    README.md        abbott           how_to_start.md

    D:\work\abbott\d_and_v>ls abbott
    abbott     manage.py

This will create a **abbott** folder in the current directory. This is where the main admin stuff
will reside. This one-liner has created a python program called **manage.py** and we usually use


```
python manage.py option
```

to manage our project, including start the server, commit the database and so on. More to come later.  Notice that there is a subfolder called the same name **abbott** along side with **manage.py**. 

## Step 2 ##

Out database module will be parallel to this folder, so it can be worked more 
directly. 

```
cd abbott

python manage.py startapp database_component
```


    D:\work\abbott\d_and_v\abbott>ls
    abbott            database_component  manage.py

    D:\work\abbott\d_and_v\abbott>ls database_component
    __init__.py  apps.py      models.py    views.py
    admin.py     migrations   tests.py


## Step 3 ##

Now we have created a folder called **database_component**. The Python program **models.py** will be where we specify our database components. 

```python
#models.py
from django.db import models

class TransLog(models.Model):
	person_id = models.CharField(max_length=100)
	Date = models.DateTimeField()
	pick_up_loc = models.CharField(max_length=200)
	drop_off_loc = models.CharField(max_length=200)
	Reason = models.CharField(max_length=200)
	first_time = models.IntegerField(default=0)

	def __str__(self):
		return self.person_id

class TransSurvey(models.Model):
	person_id = models.CharField(max_length=100)
	Date = models.DateTimeField()
	Question_1 = models.CharField(max_length=200)
	Question_2 = models.CharField(max_length=200)
	Question_3 = models.CharField(max_length=200)
	Question_4 = models.CharField(max_length=200)
	
	def __str__(self):
		return self.person_id
```

From the command line, here is what happens:

```
D:\work\abbott\d_and_v\abbott>python manage.py makemigrations database_component
Migrations for 'database_component':
  database_component\migrations\0001_initial.py
    - Create model TransLog
    - Create model TransSurvey

D:\work\abbott\d_and_v\abbott>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, database_component, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying database_component.0001_initial... OK
  Applying sessions.0001_initial... OK
  ```
 
 ## Step 4 ##
 
These database elements have been created, but they will not show up on our website yet. We need to tell Django to show them on the Admin page. 

```python
#database_component\admin.py
from django.contrib import admin

# Register your models here.
from .models import TransLog
from .models import TransSurvey
admin.site.register(TransLog)
admin.site.register(TransSurvey)
```
 
 
 ## Step 5 ##

Now if we want to see the webpage, we need to create access for ourselves. 

```
D:\work\abbott\d_and_v\abbott>python manage.py createsuperuser
Username (leave blank to use 'xiao'): xiao
Email address: xiao.chen@ucla.edu
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

## Step 6 ##

We can test our Server now. 

```
D:\work\abbott\d_and_v\abbott>python manage.py runserver
```

After loggin in, you will see the following. 

![admin page](/images_folder/step5.png)


## Step 7 ## 

Adding import and export functionality. 

This [page](https://simpleisbetterthancomplex.com/packages/2016/08/11/django-import-export.html)  provides very good step-by-step instructions. 

```
#database_component\admin.py
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import TransLog
from .models import TransSurvey
```

Also add a new file "resources.py" under the same folder. 

```
from import_export import resources
from .models import TransLog
from .models import TransSurvey

class TransLogResource(resources.ModelResource):
    class Meta:
        model = TransLog
        fields = ('id', 'person_id', 'Date', 'pick_up_loc', 'drop_off_loc', 'Reason', 'first_time')
        export_order = ('id', 'person_id', 'Date', 'pick_up_loc', 'drop_off_loc', 'Reason', 'first_time')

class TransSurveyResource(resources.ModelResource):
    class Meta:
        model = TransSurvey
        fields = ('id', 'person_id', 'Date', 'Question_1', 'Question_2', 'Question_3', 'Question_4')
        export_order = ('id', 'person_id', 'Date', 'Question_1', 'Question_2', 'Question_3', 'Question_4')
```

# this will create the buttons for import and export as well
@admin.register(TransLog)
class TransLogAdmin(ImportExportModelAdmin):
    pass

@admin.register(TransSurvey)
class TransSurveyAdmin(ImportExportModelAdmin):
    pass
```

Now if you refresh your website and click on TransLog link, you will see the following:


## Step 8 ##

When the database is messed up (or has some errors):

1. rm db.sqlite3
2. rm folder migrations
3. python manage.py makemigrations database_component
4. python manage.py migrate --fake database_component
5. python manage.py migrate 
6. python manage.py createsuperuser  -- This is a necessay step, since the database 
                                     -- needs to be rebuilt
