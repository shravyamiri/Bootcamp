class Processor:
    def process(self, lines):
        for _, line in lines:
            if "ERROR" in line:
                yield "error", line
            elif "WARN" in line:
                yield "warn", line
            else:
                yield "general", line
