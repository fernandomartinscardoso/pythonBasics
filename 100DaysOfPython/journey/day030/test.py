try:
    file = open("a_data.txt", "r")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_data.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    # This block runs only if there were no exceptions
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")