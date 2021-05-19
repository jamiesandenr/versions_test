import rollbar
from pathlib import Path

ACCESS_TOKEN = "f2187922864e45528fd750a69eb9e326"

VER = "af1a69d276400f11caa79ecd7f48766f2e0e5939"

def report(ver: str) -> None:
    rollbar.init(
        access_token=ACCESS_TOKEN,
        environment="production",
        code_version=ver,
        root=str(Path(".").parent),
    )

    try:
        1/0.0000001
    except:
        rollbar.report_exc_info()

if __name__ == "__main__":
    report(VER)