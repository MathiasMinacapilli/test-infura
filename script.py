from web3 import Web3
import sys


# Configura la URL de Infura y tu clave API

api_key = sys.argv[1]
infura_url = "https://mainnet.infura.io/v3/" + api_key
web3 = Web3(Web3.HTTPProvider(infura_url))

def get_latest_block_transactions():
    # Verifica la conexión a Infura
    if web3.is_connected():
        print("Conectado a Infura")

        # Obtiene el número del último bloque
        latest_block_number = web3.eth.block_number
        print(f"Último bloque: {latest_block_number}")

        # Obtiene las transacciones del último bloque
        latest_block = web3.eth.get_block(latest_block_number, full_transactions=True)

        # Imprime las transacciones
        transactions = latest_block["transactions"]
        print(f"\nTransacciones del último bloque ({len(transactions)} transacciones):")
        for tx in transactions:
            print(f"Hash: {tx['hash']}")
            print(f"Remitente: {tx['from']}")
            print(f"Destinatario: {tx['to']}")
            print(f"Valor: {web3.from_wei(tx['value'], 'ether')} ETH")
            print("")

    else:
        print("No se pudo conectar a Infura")

if __name__ == "__main__":
    get_latest_block_transactions()
