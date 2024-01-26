expected_result = "Hello!"
raw_file = open('./src/output.txt') # Open the txt file
file_content = raw_file.read()  # Read the content of the txt file

if file_content == expected_result:
    print("Success!")
    print(f"Expected Result: {expected_result}")
    print(f"Actual Result: {file_content}")
else:
    print("Failed")
    print(f"Expected Result: {expected_result}")
    print(f"Actual Result: {file_content}")

assert file_content == expected_result, f"The content of the TXT file is {file_content} and don't match with the expected result {expected_result}."

