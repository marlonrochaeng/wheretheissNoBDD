# Where the ISS API Automation

Using the [wheretheiss](https://wheretheiss.at/w/developer) service, you can get current, past, or future position of the ISS, get timezone information about a set of coordinates, and also get TLE data on the ISS.

In this automation project, I'm using Python + Pytest (test framework) + Requests (lib).

## Tests
13 automated test cases were created for the following endpoints:
- **satellites/[id]** 
- **satellites/[id]/positions** 
- **satellites** 
- **satellites/[id]/tles** 
- **coordinates/[lat,lon]** 

## Behaviors found during testing
 - If you pass a big timestamp (ex: 143602989200000) as a parameter to the **satellites/[id]/positions** endpoint, the API will take longer to return a 500 error without a fail message.
 - If you pass more than 10 timestamps as a parameter to the **satellites/[id]/positions** endpoint, the API will take longer to return a 500 error without a fail message.
 - If you pass another unit than **mile** or **kilometer** to the **satellites/[id]/positions** endpoint, the API will work fine but should have a validation.
 - If you pass a future timestamp or a really old one to the same endpoint, the API will work fine but should have a validation.
 - All IDs are integers, only one is string

## Prerequisite
 - Python 3.7.3 or similar
 - Git

## Installation

Clone this repository and navigate to the root folder

```bash
git clone https://github.com/marlonrochaeng/wheretheissNoBDD.git 
```

Create a virtualenv and activate it

```bash
python3 -m venv virtualenvName
virtualenvName\Scripts\activate (Windows)
source virtualenvName/bin/activate (Unix & MacOS)
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt
```

## Usage

If you want to run all of the tests:

```bash
pytest
```
If you want to run one test:
```bash
pytest tests\test_name.py
```

If you want to generate a html report:
```bash
pytest --html=report.html 
```
The result will be like:
![alt text](https://blog.cedrotech.com/hs-fs/hubfs/Imported_Blog_Media/image15-2.png?width=974&height=497&name=image15-2.png)
(source: One of my articles)

If you want to run the tests in parallel:
```bash
pytest -n <num_of_cpus>
```
By default, pytest runs tests in sequential order (alphabetical). In some scenarios, the test suite can have a great number of tests and this can lead to a large execution time. To overcome this, we can use pytest-xdist to run tests in parallel.