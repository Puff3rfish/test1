import hashlib
def sha256(s): return hashlib.sha256(s.encode()).hexdigest()
msgs = ["Vote A", "Vote B"]
for m in msgs: print(m, sha256(m))

# OUTPUT:
## DATA, HASH
## Vote A eaeac3f6c647e0156b579b59ea71ac3dbbee2b8dfab70de104dbeed3217b1e16
## Vote B 2f0ba1329645e7922015cefcac631ec6a3a78f58375e9066f338936eedaddd3b