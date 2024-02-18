# Функція довідки
def display_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")

# Функція форматування заголовка
def format_header(level, text):
    if level < 1 or level > 6:
        print("The level should be within the range of 1 to 6.")
        return ""
    return "#" * level + " " + text

# Функція форматування посилання
def format_link(label, url):
    return f"[{label}]({url})"

# Функція форматування впорядкованого списку
def format_ordered_list(num_rows, rows):
    result = ""
    for i in range(1, num_rows + 1):
        result += f"{i}. {rows[i - 1]}\n"
    return result

# Функція форматування невпорядкованого списку
def format_unordered_list(num_rows, rows):
    result = ""
    for i in range(num_rows):
        result += f"* {rows[i]}\n"
    return result

# Основна функція програми
def main():
    # Створення порожнього рядка для зберігання markdown
    markdown = ""

    while True:
        # Запитуємо у користувача вибір форматування
        user_input = input("Choose a formatter: > ")

        if user_input == "!help":
            display_help()
        elif user_input == "!done":
            # Завершуємо програму і зберігаємо результат у файл
            with open("output.md", "w") as file:
                file.write(markdown)
            print("Markdown saved in output.md.")
            break
        elif user_input == "new-line":
            markdown += "\n"
            print(markdown)
        elif user_input in ["plain", "bold", "italic", "inline-code"]:
            text_input = input("Text: > ")
            markdown += f"**{text_input}**" if user_input == "bold" else f"*{text_input}*" if user_input == "italic" else f"`{text_input}`" if user_input == "inline-code" else f"{text_input}"
            print(markdown)
        elif user_input == "header":
            level_input = input("Level: > ")
            if level_input.isdigit():
                level_input = int(level_input)
                text_input = input("Text: > ")
                markdown += format_header(level_input, text_input) + "\n"
                print(markdown)
            else:
                print("Level should be a number.")
        elif user_input == "link":
            label_input = input("Label: > ")
            url_input = input("URL: > ")
            markdown += format_link(label_input, url_input) + "\n"
            print(markdown)
        elif user_input == "ordered-list":
            num_rows = int(input("Number of rows: > "))
            if num_rows > 0:
                rows = [input(f"Row #{i + 1}: > ") for i in range(num_rows)]
                markdown += format_ordered_list(num_rows, rows)
                print(markdown)
            else:
                print("The number of rows should be greater than zero.")
        elif user_input == "unordered-list":
            num_rows = int(input("Number of rows: > "))
            if num_rows > 0:
                rows = [input(f"Row #{i + 1}: > ") for i in range(num_rows)]
                markdown += format_unordered_list(num_rows, rows)
                print(markdown)
            else:
                print("The number of rows should be greater than zero.")
        else:
            print("Unknown formatting type or command")

if __name__ == "__main__":
    main()
