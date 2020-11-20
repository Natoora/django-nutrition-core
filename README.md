# Customers Core Library

*Nutrition Core is a reusable app and provides the core functionality and attributes*


Development
----------

1. Clone django-nutrition-core project.
    ```
    git clone git@github.com:Natoora/django-nutrition-core.git
    ```

2. Install library dependencies.
    ```
    pip install -r requirements.txt
    ```

3. Execute pre-commit to install the git hooks in your .git/ directory.
    ```
    pre-commit install
    ```


Testing
-------

1. Run test script:
    ```
    (venv) $ python runtests.py
    ```

How to install django-nutrition-core into your project
-----------

1. Add "nutrition-core" to your INSTALLED_APPS setting like this::
    ``` python
    INSTALLED_APPS = [
        'nutrition_core',
    ]
    ```

2. You Custom Customer model will be inheriting from CustomerCore:
    ```python
    from nutrition_core.models import NutritionCore

    class Nutrition(NutritionCore):
        # your custom attributes and methods
        pass
    ```


Releasing
---------

1. Increment version number in setup.py

2. Commit and push changes.

3. Create release on GitHub with the version number

4. The release can then be installed into Django projects like this:
    ```
    git+https://github.com/Natoora/django-nutrition-core.git@{version number}
   ```
