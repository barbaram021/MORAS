@32767  
D=A
@min
M=D      


@0
D=A
@i
M=D

(LOOP_START)

@i
D=M
@5
D=D-A
@END
D;JGE


@i
A=M
D=M


@SKIP
D;JLE


@min
D=D-M
@SKIP
D;JGE
@i
A=M
D=M
@min
M=D

(SKIP)

@i
M=M+1
@LOOP_START
0;JMP

(END)

@min
D=M
@5
M=D


(LOOP)
@LOOP
0;JMP