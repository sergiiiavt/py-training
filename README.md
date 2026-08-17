PW test example:

    venv:
    - python -m venv .venv
    - .\.venv\Scripts\Activate.ps1

    Install:
    - python -m pip install -r requirements.txt
    - playwright install
    - npm install -g allure-commandline@2.43.0

    Execution:
    - pytest
    - pytest --headed
    - pytest --headed --slowmo 500
    - pytest --browser chromium
    - pytest --browser firefox
    - pytest --browser webkit
    - pytest --browser chromium --browser firefox --browser webkit

    Allure reporting:
    - pytest
    - allure serve allure-results

    Allure steps:
    - @allure.step("Step name") on Page Object methods


Python things:

    - python main.py