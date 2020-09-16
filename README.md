# django-scriptable-fixtures
Make fixtures in Django using python

Put the scripts folder at the root of your project and run:
```
python scripts/fixtures.py
```
or :
```
python scripts/fixtures.py some_file.py
```

If no argument is provided it will search for all '.py' files that are inside any of the fixtures folders and generate a json file for each python script.

Fixtures can then be loaded with :
```
python manage.py loaddata some_file.json
```
