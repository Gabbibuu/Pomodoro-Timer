# Pomodoro Timer

#### Video Demo: [CS50P Final Project: Pomodoro Timer](https://youtu.be/Vt-Ugt1TwGc)

#### Description:
The **Pomodoro Timer** is a simple productivity tool designed to help users manage their time more effectively using the Pomodoro Technique. The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. It's based on the idea of breaking work into intervals, traditionally 25 minutes in length, separated by short breaks. These intervals are known as *"Pomodoros"*. After completing four Pomodoros, the timer also provides a longer, more restorative 15-minute break to help users recharge and maintain productivity.

The **Pomodoro Timer** application provides the following features:
- Start, stop, reset phase and reset timers for focused work (phases), short breaks, and long breaks.
- Customizable audio notification when a timer reaches zero.
- A customizable timer length for Pomodoros (phases), short breaks, and long breaks.
- The ability to toggle the application to remain in the foreground or background.
- Clear indication of the current phase (numbered phase, short break or long break).

## Project Structure
- `project.py`: Contains the main PomodoroTimer class and the GUI setup.
- `sound.mp3`: Sound file for timer notification. This file can be replaced with any other audio file (sound still be named sound.mp3).
- `requirements.txt`: List of dependencies required to run the project.

## Design Choices
- I used the `tkinter` library for the graphical user interface (GUI) to keep the application lightweight and cross-platform.
- I incorporated `pygame` for audio notifications to ensure reliable sound playback.
- The GUI design follows a simple and intuitive layout to make it easy for users to start, stop, and reset timers.
- A toggle button allows users to keep the timer window in the foreground or background, providing flexibility for multitasking. Initially, the foreground option was fully implemented as shown in a commented line of code in the main function. However, after careful consideration, I decided to implement a button to activate and deactivate the foreground option. This change was made because the sound notifications already effectively notify the user when the timer reaches zero, making the constant foreground display less necessary.

This **Pomodoro Timer** aims to enhance productivity by helping users stay focused during work intervals and take well-deserved breaks. It can be particularly useful for students, professionals, and anyone seeking to improve time management.

Feel free to download and use this **Pomodoro Timer** to boost your productivity!

