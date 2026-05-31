from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

try:
    a=2/0
except Exception as e:
    logging.error("An error occurred: %s", str(e))
    raise USvisaException(e, sys)

# logging.info("This is an info message")