from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account
import time
import random
Account.enable_unaudited_hdwallet_features()
rpc_url = "https://sepolia.infura.io/v3/ВАШ КЛЮЧ INFURA"

web3 = Web3(Web3.HTTPProvider(rpc_url))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

mnemonic_phrase = "ВАША МНЕМОНИЧЕСКАЯ ФРАЗА"
private_key = Account.from_mnemonic(mnemonic_phrase)._private_key.hex()
account_address = Account.from_mnemonic(mnemonic_phrase).address




for i in range(1, 101):
    nonce = web3.eth.get_transaction_count(account_address)
    with open("wallets.txt", "r") as file:
        lines = file.readlines()
        receiver_address = random.choice(lines)

    receiver_address = receiver_address.strip()
    sum = random.uniform(0.000001, 0.0001)

    amount_to_send = Web3.to_wei(sum, 'ether')
    gwei = random.uniform(3, 6)
    transaction = {
        'nonce': nonce,
        'to': receiver_address,
        'value': amount_to_send,
        'gas': 21000,
        'gasPrice': web3.to_wei(gwei, 'gwei'),
        'chainId': 11155111
    }

    signed_txn = web3.eth.account.sign_transaction(transaction, private_key)

    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

    print(f'Номер транзакции: {i}', "Транзакция отправлена. Хэш транзакции:", web3.to_hex(tx_hash))

    time.sleep(60)
