from cheat.editor import Editor
from cheat.utils import Utils
import io
import os
import shutil
class Sheet:
    def __init__(self, config, sheets):
        self._config = config
        self._editor = Editor(config)
        self._sheets = sheets
    def _exists(self, sheet):
        return sheet in self._sheets.get() and os.access(self._path(sheet), os.R_OK)
    def _exists_in_default_path(self, sheet):
        default_path = os.path.join(self._config.cheat_user_dir, sheet)
        return sheet in self._sheets.get() and os.access(default_path, os.R_OK)
    def _path(self, sheet):
        return self._sheets.get()[sheet]
    def edit(self, sheet):
        if not self._exists(sheet):
            new_path = os.path.join(self._config.cheat_user_dir, sheet)
            self._editor.open(new_path)
        elif self._exists(sheet) and not self._exists_in_default_path(sheet):
            try:
                shutil.copy(self._path(sheet), os.path.join(self._config.cheat_user_dir, sheet))
            except IOError:
                Utils.die("Could not copy cheatsheet for editing.")
            self._editor.open(self._path(sheet))
        else:
            self._editor.open(self._path(sheet))
    def read(self, sheet):
        if not self._exists(sheet):
            Utils.die("No cheatsheet found for " + sheet)
        with io.open(self._path(sheet), encoding="utf-8") as cheatfile:
            return cheatfile.read()
