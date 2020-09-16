# django-scriptable-fixtures
Make fixtures in Django using python

Usage:
```
python fixtures.py
```
or :
```
python fixtures.py some_file.py
```

If no argument is provided it will search for all '.py' files that are inside any of the fixtures folders and generate a json file for each python script.

Fixtures can then be loaded with :
```
python manage.py loaddata some_file.json
```
