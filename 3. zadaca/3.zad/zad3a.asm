@10     
D=A
@R0
M=D

@20     
D=A
@R1
M=D

@R2
M=0

@R0
D=M
@R1
D=D-M
@SWAP
D;JGT

(LOOP)
    @R1       
    D=M
    @R2       
    M=M+D
    @R1       
    M=M-1
    @R0       
    D=M
    @LOOP_END 
    D-M;JGT
    @LOOP     
    0;JMP

(SWAP)
    @R0       
    D=M
    @temp
    M=D
    @R1       
    D=M
    @R0
    M=D
    @temp     
    D=M
    @R1
    M=D
    @LOOP     
    0;JMP

(LOOP_END)
    @END     
    0;JMP

(END)
    @END      
    0;JMP

    