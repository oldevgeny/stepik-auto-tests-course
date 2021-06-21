# Stepik - auto tests course

Это репозиторий для хранения домашних заданий.
Ссылка на курс: [Автоматизация тестирования с помощью Selenium и Python](https://stepik.org/course/575)

## HOW TO INSTALL:

### Python version -- 3.8.5


#### 1) Activate your virtual environment:

##### For Mac:
```python
python3 -m venv venv
source venv/bin/activate
```

##### For Windows:
```python
pip install virtualenv
virtualenv venv
venv\Scripts\activate
```


#### 2) Clone the repository to your local machine:

```python
git clone https://github.com/oldevgeny/stepik-auto-tests-course.git
```


#### 3) Install the requirements:

```python
pip install --upgrade pip
pip install -r requirements.txt
```


## START:

#### Run scripts

```python
python3 [script_path]
```

#### Run PyTests

```python
pytest scripts/selenium_scripts
# find all tests in dir scripts/selenium_scripts

pytest test_user_interface.py
# find and run all tests in file

pytest scripts/drafts.py::test_register_new_user_parametrized
# find test with name test_register_new_user_parametrized in current file in current dir and run
```
