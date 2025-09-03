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
W1Cg 
W3A 
W3B 
W2D 
R3D 
W3D 
RINFA RINFB RINFC RINFD"""

def sequence_evaluator(ref, sub):
    """This function compars sequences.

    Args:
        ref (str): reference sequence
        sub (str): submission sequence

    Returns:
        Boolean: When False, the source of error os added.
    """
    ref = [line.replace(" ", "") for line in ref.splitlines() if line.strip() != ""]
    sub = [line.replace(" ", "") for line in sub.splitlines() if line.strip() != ""]

    diff = DeepDiff(ref, sub)

    if not diff:
        return True
    else:
        return False, diff

# for testing purposes
# print(sequence_evaluator(ref, sub))

