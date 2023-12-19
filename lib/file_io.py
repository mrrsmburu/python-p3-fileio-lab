def write_file(file_name, file_content):
    
    file_name_with_extension = file_name + ".txt"

    
    with open(file_name_with_extension, 'w') as file:
        file.write(file_content)

def append_to_file(file_name, file_content):
    
    file_name_with_extension = file_name + ".txt"

    with open(file_name_with_extension, 'a') as file:
        file.write(file_content)

def read_file(file_name):
    
    file_name_with_extension = file_name + ".txt"

    
    with open(file_name_with_extension, 'r') as file:
        content = file.read()
        return content

