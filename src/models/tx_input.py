class TxInput:
    def __init__(self, prev_tx_id: str, output_index: int):
        self.prev_tx_id = prev_tx_id
        self.output_index = output_index
