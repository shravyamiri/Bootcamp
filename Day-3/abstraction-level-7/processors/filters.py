class Processor:
    def process(self, lines):
        for tag, line in lines:
            if tag in ["error", "warn", "general"]:
                yield "end", line.upper()
