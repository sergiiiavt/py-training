# Python Training

This repository has two purposes:

- `learning/` contains small standalone Python scripts created while learning and experimenting with the language.
- `automation/` contains a small Playwright + pytest UI automation example.

The learning scripts are intentionally independent examples rather than one application.

## Repository structure

```text
py-training/
├── automation/
│   ├── pages/
│   │   └── bing_search_page.py
│   ├── tests/
│   │   ├── conftest.py
│   │   └── test_bing_search.py
│   ├── pytest.ini
│   └── requirements.txt
├── learning/
│   ├── equality_identity_mutable_defaults.py
│   ├── python_basics.py
│   └── type_annotations.py
├── .gitignore
└── README.md
```

## Automation example

Run the automation project from its own directory:

```powershell
cd automation
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
playwright install
npm install -g allure-commandline@2.43.0
```

### Execute tests

```powershell
pytest
pytest --headed
pytest --headed --slowmo 500
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
pytest --browser chromium --browser firefox --browser webkit
```

### Allure reporting

```powershell
pytest
allure serve allure-results
```

Page Object methods can use Allure steps:

```python
@allure.step("Step name")
```

## Python learning scripts

Run a learning script directly from the repository root, for example:

```powershell
python learning/python_basics.py
python learning/type_annotations.py
python learning/equality_identity_mutable_defaults.py
```
