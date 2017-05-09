# Debugging and Modules Exercises

* What is a module?  
A module is a reusuable piece of code that can be separated into its own file.

* List three ways to import a module in Python.    
	Using the `import` keyword:  
	1a. `import` __filename__ # imports everything from filename
	1. `import` __filename as f__ # imports everything from filename to an alias of a shorter variable, f 
	2. `from` __function__ `import` __filename__ # imports only the function from the filename
	3. `from` __function__ `import` __filename as f__ # imports only the function from the filename and aliases the function to a shorter variable, f
  
* What is the purpose of importing?  
The purpose of importing is to keep our code DRY, reuse, and readability.

* List three examples when you would use the `random` module.  
	1. For a guess the number game
	2. For a card shuffle 
	3. For a coin toss   

* What is an `ImportError`?  
An `ImportError` will be raised when it fails to find the module definition (the thing you want to be imported)

* When would using an `OrderedDict` be useful?  
It would be useful when order of the key-value pairs matter and you care about when which key-values are added. (also if you want keys alphabetized)

* When would using a `defaultdict` be useful?  
It would be useful when you want a default value for any keys you have in a dictionary or if you want multiple values for one key.

* What is the purpose of the following code:
```python  
if __name__ == '__main__':  
	pass
```  
The purpose of the following code is to check if the module being run is the main module. If it is, we're telling it to not do anything right now (a temporary placeholder). If this is not the main module, the code inside the if will not run.