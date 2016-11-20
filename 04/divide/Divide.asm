// http://stackoverflow.com/questions/5386377/division-without-using
// Calculate (R13-R14) and assign result to D
@R14
D=M
@R13
D=M-D
///////////////////////
// Now checking special conditions:
@ZERO  // If R13-R14<0 THEN R13/R14<1, so go to (ZERO) where R15 will be set to 0 and "terminate" program.
D;JLT
@ONE  // If R13-R14==0 THEN R13/R14==1, so go to (ONE) where R15 will be set to 1 and "terminate" program.
D;JEQ

// Else, division is not trivial, Starting division process:
@R15  // Initialize R15 to be '0'
M=0
@Current  // Initialize Current to be '1'
M=1
@FIRST  // Go to (FIRST)
0;JMP

(FIRST)
	@Current  // R14 fits inside R13 at least once, so shift left Current (Multiply by 2)
	M=M<<
	@R14  // Shift left the denominator (Multiply by 2)
	M=M<<

	// Calculate (R13-R14)
	@R14
	D=M
	@R13
	D=M-D
	///////////////////////

	@MID  // If R13-R14<0 then R13/R14<1, so go to (MID)
	D;JLT
	@FIRST  // Else go to division (FIRST)
	0;JMP

(MID)
	@R14
	M=M>>
	@Current
	M=M>>
	@SECOND
	0;JMP

(HELPER1)
	// Do R13<--(R13-R14)
	@R14
	D=M
	@R13
	M=M-D
	/////////////////////
	// Do R15+=Current
	@Current
	D=M
	@R15
	M=M+D
	//////////////////
	@HELPER2
	0;JMP

(HELPER2)
	@Current
	M=M>>
	@R14
	M=M>>

	@SECOND
	0;JMP


(SECOND)
	// If Current==0 Go to (END)
	@Current  
	D=M
	@END
	D;JEQ
	////////////////////////////
	// Calculate (R13-R14)
	@R14
	D=M
	@R13
	D=M-D
	///////////////////////
	@HELPER1  // If (R13-R14>=0) go to HELPER1
	D;JGE
	@HELPER2  // Else go to HELPER2
	0;JMP
	

(ZERO)
	@R15
	M=0
	@END
	0;JMP

(ONE)
	@R15
	M=1
	@END
	0;JMP

(END)
