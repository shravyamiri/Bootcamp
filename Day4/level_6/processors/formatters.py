class snakecase:
    def process(self, lines):
        for line in lines:
            yield ("end", line.replace(" ", "_").lower())
