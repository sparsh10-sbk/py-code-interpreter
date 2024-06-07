
from filereader import FileReaderFactory
from codegenerator import generate_code
from codeexecutor import execute_code

def handle_user_request(file_path, file_type, prompt):
    try:
        file_reader = FileReaderFactory.get_file_reader(file_type)
        content = file_reader.read(file_path)
    except ValueError as e:
        return str(e)
    
    code = generate_code(prompt, content)
    result = execute_code(code)
    return result
