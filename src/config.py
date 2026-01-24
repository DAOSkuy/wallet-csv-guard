"""Central config for wallet-csv-guard."""
import os

RPC_URLS = os.getenv("RPC_URLS", "").split(",")
PRIVATE_KEYS = os.getenv("PRIVATE_KEYS", "").split(",")
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "5"))
TIMEOUT = int(os.getenv("TIMEOUT", "30"))
CHAIN_ID = int(os.getenv("CHAIN_ID", "8453"))
