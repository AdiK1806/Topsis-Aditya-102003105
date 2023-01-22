# Topsis Value Calculator
Selection of an appropriate Multiple Attribute Decision Making (MADM) method for providing a solution to a given MADM problem is always challenging endeavour. The challenge is even greater for situations where for a specific MADM problem there exist multiple MADM methods with similar degree of suitability. The Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) helps solve MADM problems.


This is a Python package implementing TOPSIS method for multi-criteria decision analysis.




## Installation

**$ pip install TOPSIS-102003105** 

In the commandline, you can write as -
    **$ python <package_name> <path to input_data_file_name> 
    <weights as strings> <impacts as strings> <result_file_name>**
	

E.g for input data file as data.csv, command will be like
    **$ python 102003105.py 102003105-data.csv "0,1,1,1,2,1" "+,-,-,+,-,+" 102003105-Result1.csv**


This will give the output in 102003105-Result1.csv file

License -> MIT