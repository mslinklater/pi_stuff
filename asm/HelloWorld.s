@
@ Assembler program to print "Hello World!"
@ to stdout
@
@ R0-R2-parameters to linux function services
@ R7 - linux function number
@

.global _start
@ address to linker

@ Set up the parameters to print hello world
@ and then call Linux to do it.

_start: mov R0, #1      @ 1 = StdOut
    ldr R1, =helloworld
    mov R2, #13     @ length of our string
    mov R7, #4      @ linux write system call
    svc 0           @ call linux to print

@ Set up thr parameters to exit the program
@ and then call linux to do it
    mov R0, #0      @ Use 0 return code
    mov R7, #1      @ Service command code 1
    svc 0

.data
helloworld:     .ascii  "Hello World!\n"
