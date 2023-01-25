<p align='center'>
  <img src='https://raw.githubusercontent.com/rzkytmgr/cemas/master/static/Screenshot%20from%202023-01-25%2021-44-20.png' alt='Cemas Scanner'>
</p>
<p align='center'>
  <img src='https://img.shields.io/github/last-commit/rzkytmgr/cemas' alt='last commit'>
  <img src='https://img.shields.io/github/license/rzkytmgr/cemas' alt='license'>
  <img src='https://img.shields.io/github/languages/code-size/rzkytmgr/cemas' alt='cemas'>
  <img src='https://img.shields.io/github/issues/rzkytmgr/cemas' alt='issues'>
  <img src='https://img.shields.io/github/issues-pr/rzkytmgr/cemas' alt='prs'>
</p>


## #
```
Bitcoin : 15y1CVhGZZowJzVHbfwNS7nAh39kXNnMdd
Paypal  : https://paypal.me/rzkytmgr
```
```
   ______ __ __  __    __  
  / _/ __|  V  |/  \ /' _/ 
 | \_| _|| \_/ | /\ |`._`. v1.0.0
  \__/___|_| |_|_||_||___/ Content Management System Mass Scanner

usage: cemas.py -t hostlist.txt [OPTIONAL]

a content management system mass scanner, 
it will separate the hosts from the list that you have into several parts according to the cms used

options:
  -h, --help       show this help message and exit
  -t , --target    specify your target files with your hosts lists
  -c , --cms       specify your target cms default: (include all cms provided by tools)
  -d , --out-dir   specify the output directory
  --timeout        specify maximum timeout when give requesting to a host
  --thread         specify max thread that you want
```


## Description
Cemas - Content Management System Mass Scaner, it will help you to parsing the host by it cms from yout list with rich feature. Built with python 3.x above `urllib3` module to do http request. for now, it's only available to scan several CMS, Wordpress, Joomla, Drupal, and Magento

## Installation

Make sure you have `python 3.x` and `pip` installed on your device, then clone it with command below
```bash
> git clone https://github.com/rzkytmgr/cemas.git && cd cemas
```
then insta the needed module listed on `requirements.txt`
```bash
> pip install -r requirements.txt
```

## Usage
Before using Cemas scaner, you should have list of host to check, you can save it anywhere you want in cemas directory. example of your list data,
```
# hostlist.txt
http://192.168.100.1/wordpres/
http://192.168.100.2/joomla/
http://192.168.100.3/drupal/
```
it separated by break line, it's mean one line one host. after you saved you list into a `.txt` file in Cemas directory, you can start Cemas scanner with command below
```bash
> python3 cemas.py -t hostlist.txt
```
Cemas is built with `argparse` module with default help command flag, it's mean you can see the available flag using command below
```bash
> python3 cemas.py --help
```
## Contribution
Feel free to make an issue or make a pull request
