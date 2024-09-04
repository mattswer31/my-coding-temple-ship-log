A. Basics of Variables:
    a. what is a variable in python?
        - container for storing data values
    b. how is mermory allocation for a variable done?
        - automatically with a garbage collector
        - stack and heap. methods/method calls and rfs are stored in stack memory. values objects in a private heap.
            - stack is the memory only needed in a function or method call. any needed variables are added onto the call stack, all deleted when the function returns. call stack moves on to next stack
            -heap memory has nothing to do with heap data structure. it is a pile of memory space available to programmers to allocate and deallocate. variables or function calls shared with multiple functions globally are stored in heap.

B. Variable Assignment:
    a. explore how to assign values to variables
        - normally without casting, python will automatically assign type
        - x = str(3)    # x will be '3'
          y = int(3)    # y will be 3
          z = float(3)  # z will be 3.0 
    b. can a variable hold multiple values?
        - arrys for large datasets
        - dictionaries when you need to associate values with unique keys
        - lists for simple that dont need specific requirements
C. Variable naming conventions
    a. research the rules and conventions for naming variables
        - must start with letter or _ , no numbers
        - the name can only contain alpha-numeric chas and _
        - case sensitive
        - x, X, lowercase, lower_score, UPPER, UPPER_SCORE, CamCase, mixedCase, Cap_Score_Ugly
    b. identify a list of reserved keywords that cant be used as variable names
        - and or not if elif else for while break as def lambda pass
          return True False try width assert class continue del except
          finally from global import in is none nonlocal raise yield async await
D. dynamic typing:
    a. how does python handle variable types?
        - variables in most languages are statically typed, initialized to a data type and any value must match. variables are not statically typed, they can be reassigned as anything. the actual typing is done automatically but can be done manually.
    b. Look into how a variable's type can change during runtime
        - explicit or implicit type conversions
E. multiple assignments:
    a. can you assign values to multiple variables in a single line?
        - yes,
        x, y , z = "orange", "blue", "crayon" or
        x = y = z = "orange", "blue", "crayon"
        print(x)
        print(y)
        print(z)

