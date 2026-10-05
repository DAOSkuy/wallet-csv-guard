"""Minimal RPC client with rotation and failover."""
import itertools

from config import RPC_URLS


class RotatingRPC:
    def __init__(self, urls=None):
        self.urls = list(urls or RPC_URLS)
        self.pool = itertools.cycle(self.urls)

    def call(self, method, params):
        body = {"jsonrpc": "2.0", "id": 1, "method": method, "params": params}
        last_err = None
        for _ in range(len(self.urls)):
            url = next(self.pool)
            try:
                return _post(url, body)
            except Exception as exc:  # noqa: BLE001
                last_err = exc
        raise last_err


def _post(url, payload):
    import json as _json
    import urllib.request

    req = urllib.request.Request(url, data=_json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=15) as r:
        data = _json.loads(r.read())
    if "error" in data:
        raise RuntimeError(data["error"])
    return data["result"]


# TODO: generalize for wallet-csv-guard


# TODO: generalize for wallet-csv-guard
