from tkinter import *
from tkinter import messagebox
import pyperclip
from data import messages, morse_code_dict


# ---------------------------- CONSTANTS ------------------------------- #

WHITE = '#FFFFFF'
BLACK = '#000000'
GREY = '#D9D9D9'
FONT_TIMES = 'Times New Roman'
FONT_CONSTANT = 'Constantia'
PADX_LEFT = 88
term_info_shown = False
mark_info_shown = False


# ---------------------------- ENCODING MECHANISM ------------------------------- #

def encode():
    encoding_result_entry.delete(0, 'end')
    encoded_word = ''
    word = encoding_entry.get()
    morse_code_keys = list(morse_code_dict.keys())
    error_shown = False
    global term_info_shown
    global mark_info_shown
    if len(word) == 0:
        messagebox.showerror('Oops', messages['empty_field_error'])
    elif word[0] == '#' and word[1:] in morse_code_keys[-4:]:
        if not term_info_shown:
            messagebox.showinfo('FYI', messages['term_info'])
            term_info_shown = True
        encoded_word += morse_code_dict[word[1:]]
    else:
        for letter in word:
            if letter.upper() in morse_code_dict:
                if letter in morse_code_keys[36:65]:
                    if not mark_info_shown:
                        messagebox.showinfo('FYI', messages['mark_info'])
                        mark_info_shown = True
                encoded_word += morse_code_dict[letter.upper()]
                encoded_word += ' '
            else:
                if not error_shown:
                    messagebox.showerror('Oops', messages['character_error'])
                    error_shown = True
    encoding_result_entry.insert(0, encoded_word)
    pyperclip.copy(encoded_word)


# ---------------------------- DECODING MECHANISM ------------------------------- #

def decode():
    decoding_result_entry.delete(0, 'end')
    decoded_word = ''
    code = decoding_entry.get()
    morse_code_values = list(morse_code_dict.values())
    error_shown = False
    info_shown = False
    global mark_info_shown
    if len(code) == 0:
        messagebox.showerror('Oops', messages['empty_field_error'])
    else:
        for part in code.split():
            for letter in morse_code_dict:
                if part == morse_code_dict[letter]:
                    if part in morse_code_values[-4:]:
                        if not info_shown:
                            messagebox.showinfo('FYI', messages['term_info'])
                            info_shown = True
                    elif part in morse_code_values[36:65]:
                        if not mark_info_shown:
                            messagebox.showinfo('FYI', messages['mark_info'])
                            mark_info_shown = True
                    decoded_word += letter.lower()
                if part not in morse_code_dict.values():
                    if not error_shown:
                        messagebox.showerror('Oops', messages['code_error'])
                        error_shown = True
        decoding_result_entry.insert(0, decoded_word)
        pyperclip.copy(decoded_word)


# ---------------------------- CLEARING MECHANISM ------------------------------- #

def clear_encoding():
    encoding_entry.delete(0, 'end')
    encoding_result_entry.delete(0, 'end')


def clear_decoding():
    decoding_entry.delete(0, 'end')
    decoding_result_entry.delete(0, 'end')


# ---------------------------- SAVING MECHANISM ------------------------------- #

def save():
    word = encoding_entry.get()
    code = decoding_entry.get()
    encoding_result = encoding_result_entry.get()
    decoding_result = decoding_result_entry.get()
    if len(word) > 0 and len(encoding_result) == 0 or len(word) == 0 and len(encoding_result) > 0:
        messagebox.showerror('Oops!', messages['empty_field_error_saving'])
    elif len(code) > 0 and len(decoding_result) == 0 or len(code) == 0 and len(decoding_result) > 0:
        messagebox.showerror('Oops!', messages['empty_field_error_saving'])
    elif len(word) == 0 and len(encoding_result) == 0 and len(code) == 0 and len(decoding_result) == 0:
        messagebox.showerror('Oops!', messages['empty_field_error_saving'])
    else:
        confirmation = messagebox.askokcancel('Please confirm!', message=f'These are the details entered:\n'
                                                                         f'{word} {encoding_result}\n'
                                                                         f'{code} {decoding_result}')
        if confirmation:
            with open('results.txt', 'a') as data_file:
                if len(encoding_result) > 0 and len(decoding_result) > 0:
                    data_file.write(f'[ {word} ] --> [ {encoding_result} ]\n'
                                    f'[ {code} ] --> [ {decoding_result} ]\n')
                elif len(encoding_result) > 0:
                    data_file.write(f'[ {word} ] --> [ {encoding_result} ]\n')
                elif len(decoding_result) > 0:
                    data_file.write(f'[ {code} ] --> [ {decoding_result} ]\n')


# ---------------------------- NIGHT MODE MECHANISM ------------------------------- #

def select_night_mode():
    if night_mode.get():
        window.config(bg=BLACK)
        morse_code_img.config(file='s_in_black.png')
        title_label.config(bg=BLACK, fg=WHITE)
        welcome_label.config(bg=BLACK, fg=WHITE)
        rules_label.config(bg=BLACK, fg=WHITE)
        add_button.config(bg=BLACK, fg=WHITE)
        night_mode_button.config(bg=BLACK, fg=WHITE, selectcolor=BLACK)
        copyright_label.config(bg=BLACK, fg=WHITE)
        # Encoding part
        encoding_label.config(bg=BLACK, fg=WHITE)
        encode_button.config(bg=BLACK, fg=WHITE)
        encoding_result_label.config(bg=BLACK, fg=WHITE)
        clear_button_encoding.config(bg=BLACK, fg=WHITE)
        # Decoding part
        decoding_label.config(bg=BLACK, fg=WHITE)
        decode_button.config(bg=BLACK, fg=WHITE)
        decoding_result_label.config(bg=BLACK, fg=WHITE)
        clear_button_decoding.config(bg=BLACK, fg=WHITE)
    else:
        window.config(bg=GREY)
        morse_code_img.config(file='s_in_grey.png')
        title_label.config(bg=GREY, fg=BLACK)
        welcome_label.config(bg=GREY, fg=BLACK)
        rules_label.config(bg=GREY, fg=BLACK)
        add_button.config(bg=GREY, fg=BLACK)
        night_mode_button.config(bg=GREY, fg=BLACK, selectcolor=WHITE)
        copyright_label.config(bg=GREY, fg=BLACK)
        # Encoding part
        encoding_label.config(bg=GREY, fg=BLACK)
        encode_button.config(bg=GREY, fg=BLACK)
        encoding_result_label.config(bg=GREY, fg=BLACK)
        clear_button_encoding.config(bg=GREY, fg=BLACK)
        # Decoding part
        decoding_label.config(bg=GREY, fg=BLACK)
        decode_button.config(bg=GREY, fg=BLACK)
        decoding_result_label.config(bg=GREY, fg=BLACK)
        clear_button_decoding.config(bg=GREY, fg=BLACK)


# ---------------------------- UI SETUP ------------------------------- #

# GENERAL PART

window = Tk()
window.title("Morse Code Converter")
window.iconbitmap('s_icon_in_black.ico')
window.config(bg=GREY)
window.columnconfigure(0, weight=3)
window.columnconfigure(3, weight=3)
window.rowconfigure(0, weight=1)
window.rowconfigure(14, weight=1)
window.state('zoomed')

canvas = Canvas(width=200, height=192, highlightthickness=0)
morse_code_img = PhotoImage(file='s_in_grey.png')
canvas.create_image(100, 92, image=morse_code_img)
canvas.grid(column=1, row=0, padx=(PADX_LEFT, 0))

title_label = Label(text='Morse Code Converter\n\n', bg=GREY, fg=BLACK, font=(FONT_TIMES, 14, 'bold'))
title_label.grid(column=1, row=1, padx=(PADX_LEFT, 0))

add_button = Button(text='Save', bg=GREY, fg=BLACK, command=save)
add_button.grid(column=1, row=7, padx=(PADX_LEFT, 0))

welcome_label = Label(text=messages['welcome_message'], bg=GREY, fg=BLACK, font=(FONT_TIMES, 12))
welcome_label.grid(column=1, row=10, padx=(PADX_LEFT, 0))

rules_label = Label(text=messages['rules_message'],
                    bg=GREY,
                    fg=BLACK,
                    font=(FONT_TIMES, 11),
                    anchor="w",
                    justify="left")
rules_label.grid(column=1, row=12, padx=(PADX_LEFT, 0))

night_mode = IntVar(value=0)
night_mode_button = Checkbutton(window,
                                text='Night Mode',
                                variable=night_mode,
                                command=select_night_mode,
                                bg=GREY,
                                fg=BLACK,
                                selectcolor=WHITE,
                                activebackground=GREY)
night_mode_button.grid(column=4, row=13, sticky=W)

copyright_label = Label(text=messages['copyright_message'], bg=GREY, fg=BLACK, font=(FONT_TIMES, 10, 'bold'))
copyright_label.grid(column=1, row=14, padx=(PADX_LEFT, 0))

# ENCODING PART

encoding_label = Label(text='Please type a word to encode.', fg=BLACK, bg=GREY, font=(FONT_CONSTANT, 9, 'bold'))
encoding_label.grid(column=0, row=2, padx=(PADX_LEFT, 0))

encoding_entry = Entry(width=25, bg=WHITE, fg=BLACK)
encoding_entry.focus()
encoding_entry.grid(column=0, row=3, padx=(PADX_LEFT, 0))

encode_button = Button(text='Encode', command=encode, bg=GREY, fg=BLACK)
encode_button.grid(column=1, row=3, sticky=W, padx=(PADX_LEFT, 0))

encoding_result_label = Label(text='Encoding result:', fg=BLACK, bg=GREY, font=(FONT_CONSTANT, 9, 'bold'))
encoding_result_label.grid(column=0, row=6, padx=(PADX_LEFT, 0))

encoding_result_entry = Entry(width=25, bg=WHITE, fg=BLACK)
encoding_result_entry.bind("<Key>", lambda a: "break")
encoding_result_entry.grid(column=0, row=7, padx=(PADX_LEFT, 0))

clear_button_encoding = Button(text='Clear', command=clear_encoding, bg=GREY, fg=BLACK)
clear_button_encoding.grid(column=1, row=7, sticky=W, padx=(PADX_LEFT, 0))

# DECODING PART

decoding_label = Label(text='Please type a code to decode.', fg=BLACK, bg=GREY, font=(FONT_CONSTANT, 9, 'bold'))
decoding_label.grid(column=3, row=2, padx=(PADX_LEFT, 0))

decoding_entry = Entry(width=25, bg=WHITE, fg=BLACK)
decoding_entry.grid(column=3, row=3, padx=(PADX_LEFT, 0))

decode_button = Button(text='Decode', command=decode, bg=GREY, fg=BLACK)
decode_button.grid(column=1, row=3, sticky=E)

decoding_result_label = Label(text=f'Decoding result:', fg=BLACK, bg=GREY, font=(FONT_CONSTANT, 9, 'bold'))
decoding_result_label.grid(column=3, row=6, padx=(PADX_LEFT, 0))

decoding_result_entry = Entry(width=25, bg=WHITE, fg=BLACK)
decoding_result_entry.bind("<Key>", lambda a: "break")
decoding_result_entry.grid(column=3, row=7, padx=(PADX_LEFT, 0))

clear_button_decoding = Button(text='Clear', command=clear_decoding, bg=GREY, fg=BLACK)
clear_button_decoding.grid(column=1, row=7, sticky=E)

window.mainloop()
