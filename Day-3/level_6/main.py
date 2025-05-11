import yaml
from engine import StateRouter

def read_input():
    # Example lines
    return iter([
        "ERROR: Disk full",
        "WARN: CPU usage high",
        "INFO: All systems go"
    ])

def main():
    with open("config.yaml") as f:
        config = yaml.safe_load(f)

    router = StateRouter(config)
    output = router.run(read_input())

    for line in output:
        print(line)

if __name__ == "__main__":
    main()
