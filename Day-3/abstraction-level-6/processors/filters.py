class only_error:
    def process(self, lines):
        for line in lines:
            if "ERROR" in line:
                yield ("end", f"[ERROR] {line}")

class only_warn:
    def process(self, lines):
        for line in lines:
            if "WARN" in line:
                yield ("end", f"[WARN] {line}")
