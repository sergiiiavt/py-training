PW test example: 

    venv:
    - python -m venv .venv   
    - .\.venv\Scripts\Activate.ps1

    Install:
    - pip install -r requirements.txt    
    - playwright install chromium

    Execution:
    - pytest tests/test_google_search.py --headed --slowmo 500

Python things:

 - main run pyhton file