from .models.tx_input import TxInput
from .models.tx_output import TxOutput
from .crypto_manager import CryptoManager

class Transaction:
    def __init__(self):
        self.inputs: list[TxInput] = []
        self.outputs: list[TxOutput] = []
        self.signature: bytes | None = None

    def add_input(self, prev_tx_id: str, output_index: int) -> None:
        self.inputs.append(TxInput(prev_tx_id, output_index))

    def add_output(self, recipient: str, amount: float) -> None:
        self.outputs.append(TxOutput(recipient, amount))

    def serialize(self) -> bytes:
        data = ""
        for txin in self.inputs:
            data += f"{txin.prev_tx_id}:{txin.output_index};"
        for txout in self.outputs:
            data += f"{txout.recipient}:{txout.amount};"
        return data.encode('utf-8')

    def sign(self, private_key) -> None:
        raw = self.serialize()
        self.signature = CryptoManager.sign_data(private_key, raw)

    def verify(self, public_key) -> bool:
        if self.signature is None:
            return False
        return CryptoManager.verify_signature(public_key, self.serialize(), self.signature)
