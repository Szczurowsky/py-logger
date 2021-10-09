import unittest
from pylogging.formatters.level import get_log_level_formatter
from pylogging.log_level import LogLevel


class TestLevel(unittest.TestCase):
    def test_info(self):
        info = get_log_level_formatter(LogLevel.INFO)
        self.assertEqual(info, '\033[1;34m [i] ' + '\033[4;34mInfo\033[m' + '\u0009')

    def test_warning(self):
        warning = get_log_level_formatter(LogLevel.WARNING)
        self.assertEqual(warning, '\033[1;33m [!] ' + '\033[4;33mWarning\033[m' + '\u0009')

    def test_error(self):
        error = get_log_level_formatter(LogLevel.ERROR)
        self.assertEqual(error, '\033[1;31m [x] ' + '\033[4;31mError\033[m' + '\u0009')


if __name__ == '__main__':
    unittest.main()
