import demistomock as demisto
from CommonServerPython import *
import traceback


def main():
    try:
        demisto.executeCommand("setIncident", {
            'id': 1255, 'details': "this message"
            })
    except Exception as ex:
        demisto.error(traceback.format_exc())
        return_error("Failed to executeCommand setIncident", error=ex)


if __name__ in ("__main__", "__builtin__", "builtins"):
    main()
