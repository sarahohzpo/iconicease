# IconicEase

IconicEase is a Python program designed to simplify the customization and arrangement of icons on the Windows desktop for better usability. It provides functionalities to list, arrange, and customize desktop icons, making it easier to keep your desktop organized.

## Features

- **List Icons**: Display all the icons currently on the Windows desktop.
- **Arrange Icons**: Automatically arrange icons based on specified criteria such as name or type.
- **Customize Icons**: Change the name of an icon or set a new position on the desktop.

## Requirements

- Python 3.x
- `pywin32` library
- `ctypes` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/iconicease.git
   ```

2. Navigate to the directory:
   ```bash
   cd iconicease
   ```

3. Install the required libraries:
   ```bash
   pip install pywin32
   ```

## Usage

1. Run the program:
   ```bash
   python iconicease.py
   ```

2. The program will list all icons on the desktop.

3. To arrange icons by name or type, modify the `arrange_icons(by='name')` method call with your preferred arrangement.

4. To customize an icon by renaming or repositioning, use the `customize_icon(icon_name, new_name=None, new_position=None)` method.

## Note

- This script is intended for Windows-based systems as it utilizes Windows-specific libraries and paths.
- Ensure that you have the necessary permissions to rename or move files on your desktop.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please create a pull request or issue for any suggestions or improvements.

## Acknowledgements

- Thanks to the contributors of the `pywin32` library for enabling Windows-specific functionalities in Python.

```

This code and readme provide a basic structure for the "IconicEase" program with core functionalities as described. The program uses the `pywin32` library to interact with Windows desktop elements.