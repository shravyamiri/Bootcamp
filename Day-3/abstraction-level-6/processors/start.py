class tag_lines:
    def process(self, lines):
        for line in lines:
            if "ERROR" in line:
                yield ("error", line)
            elif "WARN" in line:
                yield ("warn", line)
            else:
                yield ("general", line)
