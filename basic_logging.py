import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the lowest level to capture all logs
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
    datefmt="%Y-%m-%d %H:%M:%S",  # Timestamp format
    handlers=[
        logging.FileHandler("app.log"),  # Log to a file
        logging.StreamHandler()  # Log to console
    ]
)

# Create a logger
logger = logging.getLogger(__name__)

# Sample log messages
logger.debug("This is a DEBUG message")
logger.info("This is an INFO message")
logger.warning("This is a WARNING message")
logger.error("This is an ERROR message")
logger.critical("This is a CRITICAL message")

# Simulate a function that logs an exception
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logger.exception("Exception occurred while dividing by zero")

divide(10, 0)

print("Check 'app.log' for logged messages.")

#install python
#check python version: python3 --version
#Navigate to the script's directory:  cd path\to\your\script
#python basic_logging.py
#View the Log Files