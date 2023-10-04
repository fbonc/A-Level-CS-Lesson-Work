import re

def test_validate_reg():
    tests = [("1,056.12", True),
             ("56.78", True),
             ("123,456.78", True),
             ("21,000,000.12", True),
             ("1056.26", False),
             ("1,000,000.120", False),
             ("123,15.45", False)]
    
    for test in tests:  
        result = None
        result == "pass" if test[1] else "fail"
        message = f"Validating {test[0]}, Expecting {result}. Passed?: "
        match = re.search('^[0-9]{1,3}(,[0-9]{3})*[.][0-9]{2}$', test[0])
        passed = match is not None
        message += "YES" if passed == test[1] else "NO"
        print(message)
        
test_validate_reg()


