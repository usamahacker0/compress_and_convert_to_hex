import gzip
import binascii

# Function to take user input, compress it, and print the hex array
def compress_and_convert_to_hex():
    # Step 1: Get the HTML content from user input
    html_content = input("Enter your HTML content: ")
    
    # Step 2: Convert the HTML content string to bytes
    html_bytes = html_content.encode('utf-8')
    
    # Step 3: Compress the byte data using gzip
    compressed_data = gzip.compress(html_bytes)
    
    # Step 4: Convert the compressed byte data to a hexadecimal format
    hex_data = binascii.hexlify(compressed_data).decode('utf-8')
    
    # Print the hexadecimal byte array
    print("Hexadecimal byte array:")
    print(hex_data)
    
    # Optional: Format the hexadecimal byte array as a C-style PROGMEM array
    formatted_hex_array = ', '.join(f'0x{hex_data[i:i+2]}' for i in range(0, len(hex_data), 2))
    progmem_array = f'const char settingshtml[] PROGMEM = {{{formatted_hex_array}}};'
    
    # Print the PROGMEM array
    print("\nC-style PROGMEM array:")
    print(progmem_array)

# Run the function
compress_and_convert_to_hex()
