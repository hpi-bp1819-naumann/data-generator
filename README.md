# data-generator

## Setup

1. Install psycopg2 to access the database
```pip3 install psycopg2-binary```  

2. Clone the repository

## How To Use

- Open `main.py` in your prefered text editor
- Adjust the Settings for the Database

| variable	| datatype | description |
| ------------- | -------- | ----------- |
| host 		| string | host, where the database is running |
| user 		| string | username that has access to the database |
| password 	| string | password for the user |
| db\_name 	| string | name of the database |
| table\_name	| string | name of the table data data shall be added to |
| entries	| string | number of entries that shall be created |

- Set up `function_list` (see section Function List)

## Function List
The `function_list` dictionary contains an entry for each column, that shall be created. The follwing definition will create a table with two columns `att1` and `att2` where `att1` contains an index value starting at 0 and `att2` contains the square of the index.
```
function_list = {
	"att1" : {"sql_type" : "INTEGER", "function" : lambda a : str(a)},
	"att2" : {"sql_type" : "BIGINT", "function" : lambda a : str(a*a)}
	}
```
One column is specified as follows:
```
"<name>" : {"sql_type" : "<datatype>", "function" : <function>}
```

| placeholder	| description |
| ------------- | ----------- |
| name 		| The name of the column |
| datatype	| The sql datatype of the column |
| function	| The function that gets a row index and calculates a value for the column |

- __The function has to return a string value!__ In case the column shall contain a String, the returned value has to start and end with `'`. 
- There are already some functions defined, that you can use. You can find them in the `generator_functions.py`
