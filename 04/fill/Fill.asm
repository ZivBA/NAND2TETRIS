// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// Put your code here.

// create pointer to SCREEN address as 'addr'
@SCREEN
D=A
@addr
M=D

// set the loop limit to 8192 which is 32 line words times 256 lines
@8192
D=A
@limit
M=D

// main program loop
(LOOP)
	@0		// zero up the iteration counter before even 
	D=A  	// getting into one of the conditions.
	@n 		// create variable 'n' as the counter.
	M=D 	// assign n=0

	@KBD	// get keyboard input (value)
	D=M
	
	@BLACK 	// if KBD is not null, jump to BLACK label
	D;JGT

	@WHITE 	// else, jump to WHITE label
	0;JMP

// if there's any keyboard input, this loop will blacken the screen
(BLACK)

	@addr
	D=M 	// load the screen address pointer
	@n
	A=D+M 	// add to it the value of iteration counter
	M=-1 	// set the value at relevant pointer to -1

	@limit 	// load limit to D
	D=M

	@n 		// increase iteration counter
	M=M+1

	D=D-M 	// if n < limit, continue the BLACK loop
	@BLACK
	D;JGT
	
	@LOOP 	// else, return to main program loop
	0;JMP

// if there's no keyboard input, whiten the screen.
// same logic as black loop.
(WHITE)
	@addr
	D=M
	@n
	A=D+M
	M=0

	@limit
	D=M

	@n
	M=M+1

	D=D-M
	@WHITE
	D;JGT
	
	@LOOP
	0;JMP

// best practice never leave endless programm
