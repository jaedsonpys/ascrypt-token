from ascrypt import AScrypt


key = AScrypt.generate_key(64)
asc = AScrypt(key)

# gerando token
myuser = {'name': 'Jaedson', 'age': 24, 'github': 'jaedsonpys'}
mytoken = asc.new_token(myuser)

print(mytoken)

# decodificando token
mytoken_decoded = asc.decode_token(mytoken)
print(mytoken_decoded)