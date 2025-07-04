def read_marks_file(filepath):
    valid_data = {}
    skipped = 0

    try:
        with open(filepath, "r") as file:
            for line in file:
                try:
                    name, mark = line.strip().split(",")
                    if not name or not mark:
                        raise ValueError("Missing name or mark")
                    mark = float(mark)
                    valid_data[name] = mark
                except ValueError:
                    skipped += 1
    except FileNotFoundError:
        print("File not found.")
        return {}, 0

    return valid_data, skipped

def print_summary(data):
    try:
        total = 0
        for i, (name, mark) in enumerate(data.items(), 1):
            print(f"{i}. {name}: {mark}")
            total += mark
        average = total / len(data)
        print(f"\nAverage: {round(average, 2)}")
    except ZeroDivisionError:
        print("No valid data to calculate average.")


file_path = r"D:\Python Internship\Day-2\marks.txt"

marks, skipped_count = read_marks_file(file_path)
print_summary(marks)
print(f"\nSkipped entries: {skipped_count}")
