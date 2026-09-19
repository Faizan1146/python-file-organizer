# Python File Organizer

A simple Python automation tool that organizes files into categorized folders based on their file extensions.

## Features

* Automatically organizes files into categories such as Images, Documents, Music, Video, and Python.
* Supports multiple file extensions including `.jpg`, `.png`, `.jpeg`, `.pdf`, `.txt`, `.mp3`, `.wav`, `.mp4`, `.mkv`, and `.py`.
* Creates category folders automatically when needed.
* Prevents overwriting files with the same name.
* Displays unsupported file types.
* Handles invalid or non-existent folder names.

## Technologies Used

* Python
* `pathlib`
* `shutil`

## How It Works

The program starts in the current working directory and asks the user to enter the name of a folder.

It then:

1. Checks the files inside the selected folder.
2. Identifies each file's extension.
3. Matches the extension with a predefined category.
4. Creates the appropriate category folder if it does not already exist.
5. Moves the file into that category folder.
6. Reports duplicate files and unsupported file types.

## File Categories

| File Type               | Category  |
| ----------------------- | --------- |
| `.jpg`, `.png`, `.jpeg` | Images    |
| `.pdf`, `.txt`          | Documents |
| `.mp3`, `.wav`          | Music     |
| `.mp4`, `.mkv`          | Video     |
| `.py`                   | Python    |

## Example

Before running the program:

```text
MyFolder/
├── photo.jpg
├── notes.pdf
├── song.mp3
├── video.mp4
└── script.py
```

After running the program:

```text
MyFolder/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── notes.pdf
├── Music/
│   └── song.mp3
├── Video/
│   └── video.mp4
└── Python/
    └── script.py
```

## How to Run

1. Make sure Python is installed.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Run:

```bash
python file_organizer.py
```

5. Enter the name of the folder you want to organize.

## Skills Demonstrated

* Python programming
* File and directory handling
* `pathlib`
* File automation
* Dictionary-based categorization
* Exception handling
* Working with external modules
* Basic scripting and automation

## Future Improvements

Possible improvements include:

* Supporting more file extensions.
* Allowing the user to enter an absolute folder path.
* Adding a graphical user interface.
* Adding a dry-run mode before moving files.
* Creating a configuration file for custom categories.

## Author

Created as a Python automation project for my programming portfolio.

