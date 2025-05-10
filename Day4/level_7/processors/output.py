class Processor:
    def process(self, lines):
        for _, line in lines:
            print(f"[OUTPUT] {line}")
            yield "end", line
