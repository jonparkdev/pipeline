# Data-Pipeline
## UML-Diagram & Schema
**Entity-Relation Diagram**

![EER Diagram](https://lh3.googleusercontent.com/pQauyhY1vCyaRcQGDGV4OQCHMgYx5ZE2F0yj9IHz5bJTBdIXBXgcQvI19ZHqf0DZhgRanNvl5Fjd "EER Diagram")

**Schema**

![enter image description here](https://lh3.googleusercontent.com/ylAdKs-1_8n15wxx-Kz3SFjpsqHNb1fgjVkxCxjtQ2SkVQWQyhhX43bWmMsZCh27Vg8kd3rG9PIi "Schema")

## Functionality


```
Data-Pipeline$ gaia -h

usage: gaia [-h] {upload,read} filename user password

Datapipeline options, must be executed within relative path

positional arguments:
  {upload,read}  functions
  filename       * upload: name of file being uploaded --- read: name of file
                 where query result is being stored --- include .csv extension
  user           who is accessing the data base
  password       to authenticate user

optional arguments:
  -h, --help     show this help message and exit

```

## Set Up
**Data Base Initialization**

**Enabling Remote Access to DB**
- The following link provides instruction to allow remote access to server:
	* [https://bosnadev.com/2015/12/15/allow-remote-connections-postgresql-database-server/](https://bosnadev.com/2015/12/15/allow-remote-connections-postgresql-database-server/)
* The address and password can be provided upon request


**Mapping Script to PATH (FOR ALL USERS)**
Clone the repo to anywhere on your machine and run the command:
```
$ sudo ln -s $HOME/path/to/repository/inputScript.py /usr/local/bin/ANYNAMEYOUWANT
```
**Format of .csv File**
- The format of the headers should be in the following order for a battery test
```
column_order = ['name_student', 'date', 'test_name', 'name_cell', 'nom_volt',
                'nom_cap', 'current', 'timestmp', 'voltage']
```
- All fields must not be empty
