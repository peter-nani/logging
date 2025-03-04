Explanation:
logging.basicConfig: Configures logging with a specific format and output.
Log Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL.
Handlers:
FileHandler("app.log") logs messages to a file.
StreamHandler() prints logs to the console.
logger.exception: Captures exception traceback when an error occurs.
Output (Console and app.log file):


2025-03-04 12:00:00 - DEBUG - This is a DEBUG message
2025-03-04 12:00:00 - INFO - This is an INFO message
2025-03-04 12:00:00 - WARNING - This is a WARNING message
2025-03-04 12:00:00 - ERROR - This is an ERROR message
2025-03-04 12:00:00 - CRITICAL - This is a CRITICAL message
2025-03-04 12:00:00 - ERROR - Exception occurred while dividing by zero
Traceback (most recent call last):
  File "script.py", line 22, in divide
    return a / b
ZeroDivisionError: division by zero