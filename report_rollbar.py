import rollbar
from pathlib import Path

ACCESS_TOKEN = "f2187922864e45528fd750a69eb9e326"

VER = "61af549cc22df4aab1ea7819dc5ad117f6cb7c1f"

def report(ver: str) -> None:
    rollbar.init(
        access_token=ACCESS_TOKEN,
        environment="production",
        code_version=ver,
        root=str(Path(".").parent),
    )

    try:
        1/0
    except:
        rollbar.report_exc_info()

if __name__ == "__main__":
    report(VER)