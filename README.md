# HTML Compressor and Hex Converter

![HTML Compressor and Hex Converter](https://github.com/user-attachments/assets/d227203e-c744-4d75-b9b7-89f823f7e98b)

This project provides a graphical user interface (GUI) application to compress HTML content and convert it into a hexadecimal format. The compressed data is then formatted as a C-style PROGMEM array.

## Features

- Compress HTML content using gzip.
- Convert compressed data to hexadecimal format.
- Optionally format the hexadecimal data as a C-style PROGMEM array for use in embedded systems.

## Requirements

- Python 3.x
- `tkinter` (comes pre-installed with Python)
- `gzip` (comes pre-installed with Python)
- `binascii` (comes pre-installed with Python)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repository
    ```

3. Ensure you have Python 3.x installed. `tkinter`, `gzip`, and `binascii` are part of the standard library.

## Usage

1. Run the application:

    ```bash
    python your_script.py
    ```

2. Enter your HTML content into the text area labeled "Enter your HTML content."

3. Click the "Compress and Convert" button.

4. View the output in the "Output" section. The hexadecimal byte array and the C-style PROGMEM array will be displayed.

