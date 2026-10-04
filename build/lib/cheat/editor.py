from __future__ import print_function
from cheat.utils import Utils
import subprocess
class Editor:
    def __init__(self, config):
        self._config = config
    def editor(self):
        if not self._config.cheat_editor:
            Utils.die(
                "You must set a CHEAT_EDITOR, VISUAL, or EDITOR environment "
                "variable or setting in order to create/edit a cheatsheet."
            )
        return self._config.cheat_editor
    def open(self, filepath):
        editor_cmd = self.editor().split()
        try:
            subprocess.call(editor_cmd + [filepath])
        except OSError:
            Utils.die("Could not launch " + self.editor())
