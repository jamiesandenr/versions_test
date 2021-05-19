import rollbar
from pathlib import Path

ACCESS_TOKEN = "f2187922864e45528fd750a69eb9e326"

VER = "6536f48871e3cfe860bedbbb17916dc9e72d8807"

def report(ver: str) -> None:
    rollbar.init(
        access_token=ACCESS_TOKEN,
        environment="production",
        code_version=ver,
        root=str(Path(".").parent),
    )

    try:
        1/0.0000001
        d= {3:5}
        print(d[56])
    except:
        rollbar.report_exc_info()

if __name__ == "__main__":
    report(VER)