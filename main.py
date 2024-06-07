
# from responsehandler import handle_user_request
# import argparse

# def parse_arguments():
#     parser = argparse.ArgumentParser(description="Code Interpreter CLI")
#     parser.add_argument("file_path", type=str, help="Path to the input file")
#     parser.add_argument("file_type", type=str, choices=["pdf", "xlsx", "csv", "docx", "txt"], help="Type of the input file")
#     parser.add_argument("prompt", type=str, help="Prompt for code generation")
#     return parser.parse_args()

# if __name__ == "__main__":
#     args = parse_arguments()
    
#     file_path = args.file_path
#     file_type = args.file_type
#     prompt = args.prompt
    
#     result = handle_user_request(file_path, file_type, prompt)
#     print(result)
from responsehandler import handle_user_request
import argparse

def get_file_path():
    return input("Enter the path to the input file: ")

def get_file_type():
    while True:
        file_type = input("Enter the type of the input file (pdf/xlsx/csv/docx/txt): ").lower()
        if file_type in ["pdf", "xlsx", "csv", "docx", "txt"]:
            return file_type
        else:
            print("Invalid file type. Please enter one of pdf/xlsx/csv/docx/txt.")

def get_prompt():
    return input("Enter the prompt for code generation: ")

if __name__ == "__main__":
    file_path = get_file_path()
    file_type = get_file_type()
    prompt = get_prompt()
    
    result = handle_user_request(file_path, file_type, prompt)
    print(result)



