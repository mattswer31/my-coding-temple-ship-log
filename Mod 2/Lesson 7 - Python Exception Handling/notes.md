syntax error vs. exceptions
identify most common types of exceptions
try, except, else, finally
make and raise custom exceptions
analyze code to determine order of execution for multiple except blocks
manage potential runtime errors in real world apps

syntax - forgot a : or wrong ident, etc
exceptions - when syntax is fine but logic errors

NameError - using undefined variable
ValueError - wrong data type in variable (casting 'word' to int)
FileNotFoundError - file does not exist
OverflowError - calculating too large a number or at least for the var type
TypeError - mixing types, adding number to string
RuntimeError - catchall for things going wrong while running. infinite recursion is one example

try and except to catch errors and keep program running
else if nothing else triggers
finally always triggers
raise purporsefully triggers exception
can raise custom exceptions 