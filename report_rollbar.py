import rollbar
from pathlib import Path

ACCESS_TOKEN = "4a42fb9c91e64a779060fc0885c48c29"

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