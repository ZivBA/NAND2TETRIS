// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.


// if R1 or R2 are '0' at start of program, result is zero
// so directly goto ZERO case
@R1
D=M
@ZERO
D;JEQ


@R0
D=M
@ZERO
D;JEQ


// initialize sum
@R2
M=0

// add R0 to itself 'R1' times store result in R2
(LOOP)
	@R1		// address R1 to be number of iterations
	D=M 	// store in D
	@END
	D;JEQ	// if 0 iterations left, goto END

	@R0		// load R0 as the number to multiply
	D=M 	// store in D
	@R2		// load R2 as temporary sum
	M=M+D	// "SUM += R0"

	@R1		// load R1 to decrement iterations
	M=M-1 	// R1--

	@LOOP	// restart LOOP
	0;JMP


// if one of the multiplicands is '0' store 0 in R2 and goto END
(ZERO)
	@R2
	M=0
	@END
	0;JMP

(END)
	@END
	0;JMP