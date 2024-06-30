import tkinter as tk
from tkinter import scrolledtext, messagebox
import gzip
import binascii

def compress_and_convert_to_hex():
    # Get the HTML content from the text input
    html_content = input_text.get("1.0", tk.END).strip()
    
    if not html_content:
        messagebox.showerror("Input Error", "Please enter HTML content.")
        return
    
    # Step 2: Convert the HTML content string to bytes
    html_bytes = html_content.encode('utf-8')
    
    # Step 3: Compress the byte data using gzip
    compressed_data = gzip.compress(html_bytes)
    
    # Step 4: Convert the compressed byte data to a hexadecimal format
    hex_data = binascii.hexlify(compressed_data).decode('utf-8')
    
    # Optional: Format the hexadecimal byte array as a C-style PROGMEM array
    formatted_hex_array = ', '.join(f'0x{hex_data[i:i+2]}' for i in range(0, len(hex_data), 2))
    progmem_array = f'const char settingshtml[] PROGMEM = {{{formatted_hex_array}}};'
    
    # Display the hexadecimal data and PROGMEM array in the output text box
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "Hexadecimal byte array:\n")
    output_text.insert(tk.END, hex_data + "\n\n")
    output_text.insert(tk.END, "C-style PROGMEM array:\n")
    output_text.insert(tk.END, progmem_array)

# Create the main application window
app = tk.Tk()
app.title("HTML Compressor and Hex Converter")
app.geometry("600x400")

# Create and place the input text widget
input_label = tk.Label(app, text="Enter your HTML content:")
input_label.pack(pady=5)
input_text = scrolledtext.ScrolledText(app, width=70, height=10, fg="green", bg="black", insertbackground="green")
input_text.pack(pady=5)

# Create and place the convert button
convert_button = tk.Button(app, text="Compress and Convert", command=compress_and_convert_to_hex)
convert_button.pack(pady=5)

# Create and place the output text widget
output_label = tk.Label(app, text="Output:")
output_label.pack(pady=5)
output_text = scrolledtext.ScrolledText(app, width=70, height=10, fg="green", bg="black", insertbackground="green")
output_text.pack(pady=5)

# Run the application
app.mainloop()
