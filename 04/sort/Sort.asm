//procedure bubbleSort( A : list of sortable items )
//    n = length(A)
//    repeat
//       newn = 0
//       for i = 1 to n-1 inclusive do
//          if A[i-1] > A[i] then
//             swap(A[i-1], A[i])
//             newn = i
//          end if
//       end for
//       n = newn
//    until n = 0
//end procedure


@R15  // address R15, length of array.
D=M   // D = length of A
@n    // address n
M=D   // n = length(A)


D=D-1 // if array length is 1 just jump to end.
@END
D;JEQ

@REPEAT
0;JMP

(REPEAT)
  
  @n    // load n
  D=M   // D = n
  @END
  D;JEQ // goto END if n=0

  @0    // load 0
  D=A   // D = 0
  @newn // load newn
  M=D   // newn = 0

  @1    // load 1
  D=A   // D = 1
  @i    // load i
  M=D   // i = 1
  (FOR)
    @R14  // load R14, address of first array item
    D=M   // D = address of first item
    @i    // load i
    A=D+M // A = *A + i
    D=A   // D = A[i]
    @ai   // load ai
    M=D   // ai = *A[i]

    @R14   // load *A
    D=M    // D = *A
    @i     // load i
    A=M-1   // A = i-1
    A=D+A   // A = *A + (i-1)
    D=A     // D = *A + (i-1)
    @aim1
    M=D     // aim1 = *A[i-1]
    A=D
    D=M     // D = A[i-1]
    @ai     // load address of item A[i]
    A=M     // load value of item A[i]
    D=M-D   // D = A[i] - A[i-1]

    @SWAP
    D;JGT
    (CONTIN)

    @i
    M=M+1 // i++
    @n
    D=M
    @i
    D=D-M  // D = n-i

    @FOR
    D;JGT  // continue for loop until i=n-1

    // else:
    @newn
    D=M
    @n
    M=D // n = newn

    @REPEAT   // until n<=0
    D;JGT

    @END      // else end procedure.
    0;JMP






(SWAP)  //swap(A[i-1], A[i])
  @aim1
  A=M
  D=M
  @tmp
  M=D
  @ai
  A=M
  D=M
  @aim1
  A=M
  M=D

  @tmp
  D=M
  @ai
  A=M
  M=D

  @i
  D=M
  @newn
  M=D

  @CONTIN
  0;JMP




(END)

