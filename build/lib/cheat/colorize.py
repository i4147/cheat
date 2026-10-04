from __future__ import print_function
import sys
class Colorize:
    def __init__(self, config):
        self._config = config
    def search(self, needle, haystack):
        if not self._config.cheat_highlight:
            return haystack
        try:
            from termcolor import colored
        except ImportError:
            return haystack
        return haystack.replace(needle, colored(needle, self._config.cheat_highlight))
    def syntax(self, sheet_content):
        if self._config.cheat_colors is False or not sys.stdout.isatty():
            return sheet_content
        if not sheet_content.strip():
            return ""
        try:
            from pygments import highlight
            from pygments.lexers import get_lexer_by_name
            from pygments.formatters import TerminalFormatter
        except ImportError:
            return sheet_content
        first_line = sheet_content.splitlines()[0]
        lexer = get_lexer_by_name("bash")
        if first_line.startswith("```"):
            sheet_content = "\n".join(sheet_content.split("\n")[1:-2])
            try:
                lexer = get_lexer_by_name(first_line[3:])
            except Exception:
                pass
        return highlight(sheet_content, lexer, TerminalFormatter(bg=self._config.cheat_colorscheme))
