
import sys
import io
import logging

def execute_code(code):
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    try:
        exec(code)
    except Exception as e:
        logging.error(f"Error executing code: {e}")
        return str(e)
    finally:
        sys.stdout = old_stdout
    logging.info("Code executed successfully")
    return new_stdout.getvalue()
