"""Nonce tracking so parallel senders don't race each other."""
import threading


class NonceGuard:
    def __init__(self, start_nonce):
        self._nonce = start_nonce
        self._lock = threading.Lock()

    def next(self):
        with self._lock:
            n = self._nonce
            self._nonce += 1
            return n

    def rewind(self):
        with self._lock:
            self._nonce = max(0, self._nonce - 1)
