import os
import sys

from setuptools import setup

# --- Termux-aware prefix resolution --------------------------------------
# On Termux, PREFIX is typically /data/data/com.termux/files/usr
# Everything (bin, etc, share) lives under that prefix and is user-writable.
PREFIX = os.environ.get("PREFIX") or os.environ.get("TERMUX_PREFIX")
IS_TERMUX = bool(PREFIX) and "com.termux" in PREFIX

if IS_TERMUX:
    default_cheat_path = os.path.join(PREFIX, "share", "cheat")
    default_conf_dir = os.path.join(PREFIX, "etc")
else:
    default_cheat_path = "/usr/share/cheat"
    default_conf_dir = "/etc"

cheat_path = os.environ.get("CHEAT_PATH") or default_cheat_path

# --- Collect only real cheatsheet files (skip dirs / __pycache__) --------
SRC_DIR = os.path.join("cheat", "cheatsheets")
cheat_files = [
    os.path.join(SRC_DIR, f)
    for f in os.listdir(SRC_DIR)
    if os.path.isfile(os.path.join(SRC_DIR, f)) and not f.startswith(".")
]

# --- Build data_files list ----------------------------------------------
data_files = [(cheat_path, cheat_files)]

# Only ship a global config on non-Termux systems.
# Termux users are expected to use ~/.config/cheat/conf.yml instead.
conf_file = os.path.join("config", "cheat")
if not IS_TERMUX and os.path.isfile(conf_file):
    data_files.append((default_conf_dir, [conf_file]))

setup(
    name="cheat",
    version="2.5.1",
    author="Chris Lane",
    author_email="chris@chris-allen-lane.com",
    license="GPL3",
    description=(
        "cheat allows you to create and view interactive cheatsheets on the "
        "command-line. It was designed to help remind *nix system "
        "administrators of options for commands that they use frequently, "
        "but not frequently enough to remember."
    ),
    url="https://github.com/chrisallenlane/cheat",
    packages=["cheat"],
    scripts=["bin/cheats"],
    data_files=data_files,
)
