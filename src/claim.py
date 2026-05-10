"""Claim flow: build calldata -> sign -> broadcast."""
from retry import with_retry
from rpc import RotatingRPC


def build_claim_calldata(contract, policy_id):
    # selector for claim(address,uint256) placeholder
    return "0x" + contract[2:10].encode().hex()[:8] + policy_id.to_bytes(32, "big").hex()


def claim(rpc: RotatingRPC, contract, policy_id, sender, sign_fn):
    data = build_claim_calldata(contract, policy_id)
    tx = {
        "to": contract,
        "data": data,
        "from": sender,
        "gas": 180000,
    }
    signed = sign_fn(tx)
    return with_retry(lambda: rpc.call("eth_sendRawTransaction", [signed]))


# TODO: generalize for wallet-csv-guard


# TODO: generalize for wallet-csv-guard
