from deepdiff import DeepDiff 

sub="""S = W0A W0B W0C W0D
R1C 
R1D 
R2C 
R3A 
W1A 
W1D 
R3B 
W2B 
R2D 
W1C 
W3A 
W3B 
W2D 
R3D 
W3D 
RINFA RINFB RINFC RINFD"""

ref="""S = W0A W0B W0C W0D
R1C 
R1D 
R2C 
R3A 
W1A 
W1D 
R3B 
W2B 
R2D 
W1C 
W3A 
W3B 
W2D 
R3D 
W3D 
RINFA RINFB RINFC RINFD"""

refs = [line.replace(" ", "") for line in ref.splitlines() if line.strip() != ""]
subs = [line.replace(" ", "") for line in sub.splitlines() if line.strip() != ""]

dif = DeepDiff(refs, subs)
print(dif)
print(subs == refs)


