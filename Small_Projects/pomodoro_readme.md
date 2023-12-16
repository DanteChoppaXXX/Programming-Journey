Pomodoro Timer
This program implements a Pomodoro timer to help with time management using the Pomodoro technique.

Overview
The Pomodoro technique uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks. It is based on the tomato-shaped kitchen timer. This program allows setting timers for Pomodoro sessions (25 minutes), short breaks (5 minutes), and a longer break (15 minutes) after every 4 Pomodoros.

Features
    Timers for Pomodoro, short break, and long break that can be started, paused, reset
    Counter to track number of Pomodoros completed
    Ability to skip current timer interval
    Tab interface to switch between timers

Files
    pomodoro_timer.py - Main program file containing the PomodoroTimer class

Classes
PomodoroTimer
    The main class that initializes the GUI and timers.

Methods
    __init__() - Sets up GUI elements like tabs, labels, buttons
    start_timer_thread() - Starts timer countdown in separate thread
    start_timer() - Runs timer countdown logic
    reset_clock() - Resets all timers to initial values
    skip_clock() - Skips to next timer interval

Usage
To use, run pomodoro_timer.py. Click Start to begin a timer session. Use the tabs to switch between Pomodoro, short break, and long break timers. Click Skip to advance to the next interval. Click Reset to restart all timers.