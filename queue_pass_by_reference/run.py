from inputModule import *

kmers = strQueue()
params = IntVector([21])

# params.push_back(21)

seq = "ATGAGGGGGATGCCCCTCTTTGAGCCCAAGGACGTAGCCTATATTTTGCAACGCGTGAC"

mod = inputModuleDefault()
mod.setParams(params)
mod.fill_q(kmers, seq)

for i in range(kmers.size()):
    print ("%d: %s") % (i+1, kmers.front())
    kmers.pop()

qkmers = strQueue()
skip_params = IntVector([2,4,21])

skipmers = InputModuleSkipmers()
skipmers.setParams(skip_params)
skipmers.fill_q(qkmers, seq)

for i in range(qkmers.size()):
    print ("%d: %s") % (i+1, qkmers.front())
    qkmers.pop()
