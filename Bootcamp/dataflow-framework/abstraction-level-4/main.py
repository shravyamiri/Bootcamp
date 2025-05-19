from processors import to_upper, LineCounter, JoinEveryNLines, SplitByDelimiter

def run_pipeline(lines, processors):
    for processor in processors:
        lines = processor(lines)
    return lines


if __name__ == "__main__":
    input_lines = iter([
        "hello world",
        "foo bar",
        "python|java|c++",
        "stream processing"
    ])

    processors = [
        LineCounter(),                    # stateful
        to_upper,                         # stateless
        SplitByDelimiter("|"),            # fan-out
        JoinEveryNLines(2)                # fan-in
    ]

    output = run_pipeline(input_lines, processors)

    for line in output:
        print(line)
