from pylogging.log_level import LogLevel, LogLevelError


def get_log_level_formatter(log_level: LogLevel) -> str:
    if log_level is LogLevel.INFO:
        return '\033[1;34m [i] ' + '\033[4;34mInfo\033[m' + '\u0009'
    if log_level is LogLevel.WARNING:
        return '\033[1;33m [!] ' + '\033[4;33mWarning\033[m' + '\u0009'
    if log_level is LogLevel.ERROR:
        return '\033[1;31m [x] ' + '\033[4;31mError\033[m' + '\u0009'
    raise LogLevelError("Wrong log level (INFO, WARNING, ERROR)")
