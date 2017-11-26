import datetime
import logging

# LOGGING ----------------------------------------------------------------
filename = "logs/logfile {}.log".format(datetime.date.today())
handler = logging.FileHandler(filename, "a")
frm = logging.Formatter("%(asctime)s [%(levelname)-8s] [%(funcName)-20s] [%(lineno)-4s] %(message)s", 
                          "%d.%m.%Y %H:%M:%S") 
handler.setFormatter(frm)
logger = logging.getLogger() 
logger.addHandler(handler)

"""
+----------+---------------+
| Level    | Numeric value |
+----------+---------------+
| CRITICAL |            50 |
| ERROR    |            40 |
| WARNING  |            30 |
| INFO     |            20 |
| DEBUG    |            10 |
| NOTSET   |             0 |
+----------+---------------+
"""

logger.setLevel(logging.DEBUG)

# LOGGING ----------------------------------------------------------------

logging.debug("Test: Debug")
logging.info("Test: Info")
logging.warning("Test: Warning")
logging.error("Test: Error")
logging.critical("Test: Critical")

try:
    1 / 0
except ZeroDivisionError:
    logging.exception("Test: Exception.")
