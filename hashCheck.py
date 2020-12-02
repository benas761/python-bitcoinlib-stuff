from bitcoin.rpc import RawProxy
from hashlib import sha256

p = RawProxy()
blockNum = input("write a block's number:\n")
block = p.getblock(p.getblockhash(blockNum))
header = format(block['nonce'], 'x') + str(block['bits']) + format(block['time'], 'x') + str(block['merkleroot']) + str(block['previousblockhash']) + str(block['versionHex'])

# convert to little indian
indian_header = ""
header = header[::-1]
for i in range(0, len(header), 2):
    indian_header += header[i+1]
    indian_header += header[i]

# hashing, "borrowed" from https://en.bitcoin.it/wiki/Block_hashing_algorithm
header_binary = indian_header.decode('hex')
hash = sha256(sha256(header_binary).digest()).digest()
hash = hash[::-1].encode('hex_codec')

print("\nGotten hash:\n" + hash)
print("Block's hash:\n" + block['hash'])
print("Are they the same?")
print(hash == block['hash'])