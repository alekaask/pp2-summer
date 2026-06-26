import json
import re
from decimal import Decimal
from pathlib import Path


def regex_examples():
    print("Regex examples")
    print("search:", re.search(r"Python", "I love Python").group())
    print("findall:", re.findall(r"\d+", "Price 10 and 20"))
    print("split:", re.split(r"\s+", "one two three"))
    print("sub:", re.sub(r"cat", "dog", "cat and cat"))

    print("\nMetacharacters:")
    print(re.search(r"^H.*d$", "Hello"))

    print("\nSpecial sequences:")
    print(re.findall(r"\d+", "I have 2 cats and 10 dogs"))

    print("\nQuantifiers:")
    print(re.findall(r"\w{2,4}", "ab cdef ghijk"))


def read_receipt(path):
    return Path(path).read_text(encoding="utf-8")


def parse_prices(text):
    pattern = r"\b\d[\d\s]*,\d{2}\b"
    matches = re.findall(pattern, text)
    return [match.strip() for match in matches]


def parse_product_names(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    products = []
    for index, line in enumerate(lines):
        if re.fullmatch(r"\d+\.", line):
            if index + 1 < len(lines):
                next_line = lines[index + 1].strip()
                if next_line and not re.fullmatch(r"Стоимость", next_line):
                    products.append(next_line)
    return products


def parse_total_amount(text):
    match = re.search(r"ИТОГО:\s*(\d[\d\s]*,\d{2})", text)
    if match:
        return match.group(1).strip()
    return None


def parse_datetime(text):
    match = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2})", text)
    if match:
        return match.group(1)
    return None


def parse_payment_method(text):
    match = re.search(r"Банковская\s+карта", text)
    if match:
        return match.group(0)
    return None


def format_amount(value):
    return str(Decimal(value.replace(" ", "").replace(",", ".")))


def build_structured_output(text):
    prices = parse_prices(text)
    product_names = parse_product_names(text)
    total_amount = parse_total_amount(text)
    date_time = parse_datetime(text)
    payment_method = parse_payment_method(text)

    return {
        "prices": [format_amount(price) for price in prices],
        "product_names": product_names,
        "total_amount": format_amount(total_amount) if total_amount else None,
        "date_time": date_time,
        "payment_method": payment_method,
    }


def run_regex_exercises():
    print("\nRegex exercises")

    samples = [
        ("1. Matches 'a' followed by zero or more 'b's", r"ab*", ["a", "ab", "abb", "abbb"]),
        ("2. Matches 'a' followed by two to three 'b's", r"ab{2,3}", ["abb", "abbb", "aabbb"]),
        ("3. Lowercase letters joined by underscore", r"[a-z]+(?:_[a-z]+)+", ["a_b", "hello_world", "python_regex"]),
        ("4. One uppercase letter followed by lowercase letters", r"[A-Z][a-z]+", ["Python", "CamelCase", "Hello"]),
        ("5. 'a' followed by anything ending in 'b'", r"a.*b$", ["acb", "a123b", "aXYZb"]),
    ]

    for label, pattern, values in samples:
        print(f"\n{label}")
        for value in values:
            print(value, "->", bool(re.fullmatch(pattern, value)))

    print("\n6. Replace space, comma, or dot with a colon")
    text = "hello, world. python"
    print(re.sub(r"[\s,.]", ":", text))

    print("\n7. Snake case to camel case")
    snake = "hello_world_python"
    parts = snake.split("_")
    camel = parts[0] + "".join(word.capitalize() for word in parts[1:])
    print(camel)

    print("\n8. Split a string at uppercase letters")
    mixed = "helloWorldPython"
    print(re.sub(r"(?=[A-Z])", " ", mixed))

    print("\n9. Insert spaces between words starting with capital letters")
    text2 = "HelloWorldPython"
    print(re.sub(r"(?=[A-Z])", " ", text2).strip())

    print("\n10. Camel case to snake case")
    camel = "camelCaseString"
    print(re.sub(r"(?<!^)(?=[A-Z])", "_", camel).lower())


def main():
    regex_examples()
    run_regex_exercises()

    receipt_path = Path(__file__).with_name("raw.txt")
    receipt_text = read_receipt(receipt_path)

    print("\nReceipt parsing results")
    print("1. Extract all prices")
    print(parse_prices(receipt_text))

    print("\n2. Find all product names")
    print(parse_product_names(receipt_text))

    print("\n3. Calculate total amount")
    print(parse_total_amount(receipt_text))

    print("\n4. Extract date and time information")
    print(parse_datetime(receipt_text))

    print("\n5. Find payment method")
    print(parse_payment_method(receipt_text))

    print("\n6. Structured output")
    print(json.dumps(build_structured_output(receipt_text), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
