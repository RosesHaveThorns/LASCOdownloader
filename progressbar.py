"""
 Progress Bar
-------------
Provides console progress bar functionality.

Usage:
    Call start_progress(title) immediatley before action
    Call progress(x) after every step
    Call end_progress() after action is complete

Based on code from https://stackoverflow.com/a/6169274
"""

import sys

def start_progress(title):
    """
    Prints beggining of a console progress bar.

    Args:
        title: string, name of progress bar
    """
    global progress_x
    sys.stdout.write(title + ": [" + "-"*40 + "]" + chr(8)*41)
    sys.stdout.flush()
    progress_x = 0

def progress(x):
    """
    Updates a console progress bar with new progress.

    Args:
        x: percentage of total progress made
    """
    global progress_x
    x = int(x * 40 // 100)
    sys.stdout.write("#" * (x - progress_x))
    sys.stdout.flush()
    progress_x = x

def end_progress():
    """Prints end of progress bar after action completion"""
    sys.stdout.write("#" * (40 - progress_x) + "] DONE\n")
    sys.stdout.flush()