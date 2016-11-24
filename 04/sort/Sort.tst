//Proudly written by ITAI SHALOM
// File name: projects/04/Sort/Sort.tst

load Sort.hack,
output-file Sort.out,
compare-to Sort.cmp,
output-list RAM[2048]%D2.6.2 RAM[2049]%D2.6.2 RAM[2050]%D2.6.2 RAM[2051]%D2.6.2 RAM[2052]%D2.6.2 ;

set RAM[14] 2048,   // Set test arguments
set RAM[15] 5,

set RAM[2048] 6,   // Set test arguments
set RAM[2049] 3,
set RAM[2050] 8,
set RAM[2051] 9,
set RAM[2052] 5,
repeat 500 {
  ticktock;
}
output;

set PC 0,
set RAM[2048] 9,   // Set test arguments
set RAM[2049] 8,
set RAM[2050] 7,
set RAM[2051] 6,
set RAM[2052] 5,
repeat 500 {
  ticktock;
}
output;

set PC 0,
set RAM[2048] 11,   // Set test arguments
set RAM[2049] 15,
set RAM[2050] 9,
set RAM[2051] 2,
set RAM[2052] 0,
repeat 500 {
  ticktock;
}

output;

set PC 0,
set RAM[2048] -2,   // Set test arguments
set RAM[2049] 5,
set RAM[2050] 6,
set RAM[2051] 1,
set RAM[2052] 6,
repeat 500 {
  ticktock;
}
output;

set PC 0,
set RAM[2048] -1,   // Set test arguments
set RAM[2049] 0,
set RAM[2050] 1,
set RAM[2051] 2,
set RAM[2052] 3,
repeat 700 {
  ticktock;
}

output;

set PC 0,
set RAM[14] 2050,   // Set test arguments
set RAM[15] 1,

set RAM[2048] 6,   // Set test arguments
set RAM[2049] 3,
set RAM[2050] 8,
set RAM[2051] 9,
set RAM[2052] 5,
repeat 500 {
  ticktock;
}
output;

set PC 0,
set RAM[14] 2049,   // Set test arguments
set RAM[15] 3,

set RAM[2048] 6,   // Set test arguments
set RAM[2049] 5,
set RAM[2050] 9,
set RAM[2051] 7,
set RAM[2052] 9,
repeat 500 {
  ticktock;
}
output;