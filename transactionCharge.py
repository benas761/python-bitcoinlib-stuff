from bitcoin.rpc import RawProxy
p = RawProxy()

def decodeTransaction(transaction_id):
    raw_tx = p.getrawtransaction(transaction_id)
    decoded_tx = p.decoderawtransaction(raw_tx)
    return decoded_tx


sumIn = sumOut = 0
decoded_transaction = decodeTransaction(raw_input("transaction's hash:\n"))

for i in decoded_transaction['vout']:
    sumOut += i['value']

for i in decoded_transaction['vin']:
    # the source transaction
    decoded_input_transaction = decodeTransaction(i['txid'])
    # ['vout'] - a list of outputs
    # [i['vout']] - an output that is connected to the address
    # ['value'] - the final output sum
    sumIn += decoded_input_transaction['vout'][i['vout']]['value']

print("Transaction's fee is " + str(sumIn-sumOut))
# thanks, https://bitcoinj.org/working-with-transactions
