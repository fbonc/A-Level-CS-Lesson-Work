import re

def test_validate_reg():
    tests = [("1,056.12", "pass"),
             ("56.78", "pass"),
             ("123,456.78", "pass"),
             ("21,000,000.12", "pass"),
             ("1056.26", "fail"),
             ("1,000,000.120", "fail"),
             ("123,15.45", "fail")]
    
    for test in tests:
        message = f"Validating {test[0]}, Expecting {test[1]}. Result: "
        match = re.search('^[0-9]{1,3}(,[0-9]{3})*[.][0-9]{2}$', test[0])
        if match:
            message += "PASS"
        else:
            message += "FAIL"
        print(message)
        
test_validate_reg()


