import customtkinter
import secrets
import string


# ============================================================
# PASSWORD GENERATOR
# ============================================================

def generate_password(
    length,
    use_lowercase,
    use_uppercase,
    use_numbers,
    use_symbols
):
    try:
        length = int(length)
    except (TypeError, ValueError):
        raise ValueError("Password length must be a number.")

    if length < 12 or length > 64:
        raise ValueError("Password length must be between 12 and 64.")

    characters = ""

    if use_lowercase:
        characters += string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("Select at least one character type.")

    selected_categories = sum([
        use_lowercase,
        use_uppercase,
        use_numbers,
        use_symbols
    ])

    if length < selected_categories:
        raise ValueError(
            "Password length is too short for the selected options."
        )

    password = []

    # Guarantee at least one character from every
    # selected category.
    if use_lowercase:
        password.append(
            secrets.choice(string.ascii_lowercase)
        )

    if use_uppercase:
        password.append(
            secrets.choice(string.ascii_uppercase)
        )

    if use_numbers:
        password.append(
            secrets.choice(string.digits)
        )

    if use_symbols:
        password.append(
            secrets.choice(string.punctuation)
        )

    # Fill remaining characters
    remaining = length - len(password)

    for _ in range(remaining):
        password.append(
            secrets.choice(characters)
        )

    # Securely shuffle the password
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


# ============================================================
# PASSWORD STRENGTH
# ============================================================

def calculate_strength(password):
    score = 0

    length = len(password)

    has_lowercase = any(c.islower() for c in password)
    has_uppercase = any(c.isupper() for c in password)
    has_number = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    if length >= 12:
        score += 1

    if length >= 16:
        score += 1

    if length >= 20:
        score += 1

    if has_lowercase:
        score += 1

    if has_uppercase:
        score += 1

    if has_number:
        score += 1

    if has_symbol:
        score += 1

    if score <= 2:
        return "Weak"

    elif score <= 4:
        return "Fair"

    elif score <= 6:
        return "Strong"

    else:
        return "Very Strong"


# ============================================================
# GUI FUNCTIONS
# ============================================================

def update_length(value):
    length = int(value)

    length_label.configure(
        text=f"Password Length: {length}"
    )


def generate_button_clicked():
    try:
        length = int(length_slider.get())

        use_lowercase = bool(lowercase_checkbox.get())
        use_uppercase = bool(uppercase_checkbox.get())
        use_numbers = bool(numbers_checkbox.get())
        use_symbols = bool(symbols_checkbox.get())

        password = generate_password(
            length,
            use_lowercase,
            use_uppercase,
            use_numbers,
            use_symbols
        )

        password_entry.delete(0, "end")
        password_entry.insert(0, password)

        strength = calculate_strength(password)

        strength_label.configure(
            text=f"Strength: {strength}"
        )

        status_label.configure(
            text="Password generated successfully."
        )

    except ValueError as error:
        status_label.configure(
            text=str(error)
        )


def copy_password():
    password = password_entry.get()

    if not password:
        status_label.configure(
            text="There is no password to copy."
        )
        return

    app.clipboard_clear()
    app.clipboard_append(password)
    app.update()

    status_label.configure(
        text="Password copied to clipboard."
    )


def toggle_password_visibility():
    global password_visible

    if password_visible:
        password_entry.configure(show="•")
        show_button.configure(text="Show")
        password_visible = False

    else:
        password_entry.configure(show="")
        show_button.configure(text="Hide")
        password_visible = True


# ============================================================
# APPLICATION SETTINGS
# ============================================================

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


# ============================================================
# MAIN WINDOW
# ============================================================

app = customtkinter.CTk()

app.title("Password Generator")
app.geometry("600x600")
app.minsize(500, 550)


# ============================================================
# TITLE
# ============================================================

title_label = customtkinter.CTkLabel(
    app,
    text="PASSWORD GENERATOR",
    font=("Arial", 26, "bold")
)

title_label.pack(pady=(30, 20))


# ============================================================
# PASSWORD ENTRY
# ============================================================

password_entry = customtkinter.CTkEntry(
    app,
    width=450,
    height=40,
    font=("Arial", 16),
    show=""
)

password_entry.pack(pady=10)


# ============================================================
# SHOW / HIDE BUTTON
# ============================================================

show_button = customtkinter.CTkButton(
    app,
    text="Hide",
    width=100,
    command=toggle_password_visibility
)

show_button.pack(pady=(0, 15))


# ============================================================
# PASSWORD LENGTH
# ============================================================

length_label = customtkinter.CTkLabel(
    app,
    text="Password Length: 16",
    font=("Arial", 15)
)

length_label.pack(pady=(10, 5))


length_slider = customtkinter.CTkSlider(
    app,
    from_=12,
    to=64,
    number_of_steps=52,
    command=update_length
)

length_slider.set(16)
length_slider.pack(
    fill="x",
    padx=75,
    pady=10
)


# ============================================================
# CHARACTER OPTIONS
# ============================================================

options_label = customtkinter.CTkLabel(
    app,
    text="Character Options",
    font=("Arial", 16, "bold")
)

options_label.pack(pady=(15, 5))


options_frame = customtkinter.CTkFrame(app)

options_frame.pack(pady=10)


lowercase_checkbox = customtkinter.CTkCheckBox(
    options_frame,
    text="Lowercase"
)

lowercase_checkbox.grid(
    row=0,
    column=0,
    padx=25,
    pady=8
)


uppercase_checkbox = customtkinter.CTkCheckBox(
    options_frame,
    text="Uppercase"
)

uppercase_checkbox.grid(
    row=0,
    column=1,
    padx=25,
    pady=8
)


numbers_checkbox = customtkinter.CTkCheckBox(
    options_frame,
    text="Numbers"
)

numbers_checkbox.grid(
    row=1,
    column=0,
    padx=25,
    pady=8
)


symbols_checkbox = customtkinter.CTkCheckBox(
    options_frame,
    text="Symbols"
)

symbols_checkbox.grid(
    row=1,
    column=1,
    padx=25,
    pady=8
)


# Select all options by default
lowercase_checkbox.select()
uppercase_checkbox.select()
numbers_checkbox.select()
symbols_checkbox.select()


# ============================================================
# STRENGTH
# ============================================================

strength_label = customtkinter.CTkLabel(
    app,
    text="Strength: —",
    font=("Arial", 15, "bold")
)

strength_label.pack(pady=(15, 5))


# ============================================================
# BUTTONS
# ============================================================

button_frame = customtkinter.CTkFrame(app)

button_frame.pack(pady=15)


generate_button = customtkinter.CTkButton(
    button_frame,
    text="Generate Password",
    width=180,
    height=40,
    command=generate_button_clicked
)

generate_button.grid(
    row=0,
    column=0,
    padx=10
)


copy_button = customtkinter.CTkButton(
    button_frame,
    text="Copy",
    width=120,
    height=40,
    command=copy_password
)

copy_button.grid(
    row=0,
    column=1,
    padx=10
)


# ============================================================
# STATUS
# ============================================================

status_label = customtkinter.CTkLabel(
    app,
    text="Ready",
    font=("Arial", 12)
)

status_label.pack(pady=5)


# ============================================================
# INITIAL STATE
# ============================================================

password_visible = True


# ============================================================
# START APPLICATION
# ============================================================

app.mainloop()