# Contributing to the Image Trimmer Project
If you like this project and want to make it better, please help out. It could
be as simple as sending [@donkirkby] a nice note on Twitter, you could report a
bug, or pitch in with some development work. Check if there are some issues
labeled as [good first issues] or [help wanted].

[@donkirkby]: https://hachyderm.io/@donkirkby
[good first issues]: https://github.com/donkirkby/image-trimmer/labels/good%20first%20issue
[help wanted]: https://github.com/donkirkby/image-trimmer/labels/help%20wanted

## Bug Reports and Enhancement Requests
Please create issue descriptions [on GitHub][issues]. Be as specific as possible.
Which version are you using? What did you do? What did you expect to happen? Are
you planning to submit your own fix in a pull request? Please include a puzzle
definition text file if that helps recreate the problem.

[issues]: https://github.com/donkirkby/image-trimmer/issues?state=open

## PySide6 Tools
To edit the GUI, do the following:

1. Download and install [Qt Creator].
2. Run Qt Creator, and open the `.ui` file for the screen you want to change.
3. Read the [Qt Designer documentation], and make the changes you want.
4. Compile the `.ui` file into a Python source file with a command like this:

        pyside6-uic -o main_window.py main_window.ui

To add a new screen to the project:

1. In Qt Creator choose New File from the File menu.
2. In the Files and Classes: Qt section, choose Qt Designer Form.
3. Select a widget type, like "Widget", and choose a file name.


[Qt Creator]: https://www.qt.io/download-qt-installer
[Qt Designer documentation]: https://doc.qt.io/qt-5/designer-quick-start.html
