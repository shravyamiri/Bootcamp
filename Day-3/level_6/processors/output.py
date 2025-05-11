class terminal:
    def process(self, lines):
        for line in lines:
            yield ("end", f"[OUT] {line}")
