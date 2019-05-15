# Student-interview-solution
My solution to the post-interview coding problem involves a python script-"PythonAttempt.py" which takes in two input paramters.
The first is a csv input file, and the second is a location to write a now converted json file.

## How to run the program
	You will need to have a python interpreter installed on your machine. You can download it easily from https://www.python.org/downloads/
	The python script takes two parameters, -i <input.csv file location> and -o <output.json file location>
	You need to tell the script where your input csv file is located on your machine, and also where you want your output to be,
	otherwise an error will occur.
	Note: Output file location must contain entire file name, even if it hasn't been created yet. Example: ..<desiredpath>/kerbals.json
	
**In windows**
	1. Open the cmd and locate your python.exe. Default location is "C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python37\python.exe"
	2. Run the command: <path to python.exe from step 1.> <path to PythonAttempt.py> -i InputFileLocation -o OutputFileLocation
	Example: C:\Users\alexs\AppData\Local\Programs\Python\Python37\python.exe PythonAttempt.py -i kerbals.csv -o kerbals.json

**Mac/Linux**
	1. From the command line, locate your folder with PythonAttempt.py and kerbals.csv
	2. Run the command: python PythonAttempt.py -i kerbals.csv -o kerbals.json
	
## Results
	The program should create a .json file that has converted the kerbals.csv into the json format. It is "pretty printed" so it can be easily read by humans, 
	and is also displayed in the console. 
	
	Note: I used a windows machine and it works here, but I do not have a Mac. I did however test it on my schools server which uses a Linux shell and 
	the first time I ran it, it only printed the last half of the .json file to the console. I ran it again and it displayed the entire file as expected.
	I don't know why it did this, but the outputted file was correct both times, so it was probably just a rare fluke.
