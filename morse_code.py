import tkinter as tk

root = tk.Tk()
root.title("Kod Morsa")
root.geometry("500x400")

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}


def encrypt(text):
    morse_code = ''
    for letter in text.upper():
        morse_code += MORSE_CODE_DICT.get(letter, '?') + ' '
    return morse_code.strip()


def decrypt(morse_code):
    reverse_dict = {value: key for key, value in MORSE_CODE_DICT.items()}
    text = ''
    for code in morse_code.split():
        text += reverse_dict.get(code, '?')
    return text


def encrypt_action():
    text = input_text.get("1.0", "end-1c")
    result = encrypt(text)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", result)


def decrypt_action():
    morse_code = input_text.get("1.0", "end-1c")
    result = decrypt(morse_code)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", result)


input_label = tk.Label(root, text="Wpisz tekst lub kod morsa:")
input_label.pack(pady=10)
input_text = tk.Text(root, height=5, width=60)
input_text.pack(pady=5)


output_label = tk.Label(root, text="Wynik:")
output_label.pack(pady=10)
output_text = tk.Text(root, height=5, width=60)
output_text.pack(pady=5)


encrypt_button = tk.Button(root, text="zaszyfruj", command=encrypt_action)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="odszyfruj", command=decrypt_action)
decrypt_button.pack(pady=10)

root.mainloop()