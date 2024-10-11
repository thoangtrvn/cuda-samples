
#ncu --set full -f -o profile bin/x86_64/linux/release/matrixMul
ncu --set full --call-stack --nvtx -f -o profile bin/x86_64/linux/release/matrixMul
