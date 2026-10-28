	.file	"rv_kernel.c"
	.option pic
	.attribute arch, "rv32i2p1_m2p0_zmmul1p0_zbb1p0"
	.attribute unaligned_access, 0
	.attribute stack_align, 16
	.text
	.align	2
	.globl	sw_gotoh
	.type	sw_gotoh, @function
sw_gotoh:
.LFB1:
	.cfi_startproc
	blt	a3,zero,.L2
	lla	a5,H.1+4
	slli	a7,a3,2
	li	a6,-999424
	add	a7,a7,a5
	addi	a6,a6,-576
	lla	a5,H.1
	lla	a4,E.0
.L3:
	sw	zero,0(a5)
	sw	a6,0(a4)
	addi	a5,a5,4
	addi	a4,a4,4
	bne	a5,a7,.L3
.L2:
	ble	a1,zero,.L4
	mv	t0,a0
	add	t2,a0,a1
.L5:
	bgt	a3,zero,.L22
	addi	t0,t0,1
	bne	t0,t2,.L5
.L4:
	li	a0,0
	ret
.L22:
	addi	sp,sp,-16
	.cfi_def_cfa_offset 16
	sw	s0,12(sp)
	.cfi_offset 8, -4
	add	t6,a2,a3
	li	a0,0
.L8:
	li	a1,-999424
	lbu	s0,0(t0)
	addi	a1,a1,-576
	mv	t1,a2
	lla	a7,H.1+4
	lla	a6,E.0+4
	li	a3,0
	li	t5,0
	j	.L7
.L12:
	mv	t5,t3
.L7:
	lbu	a5,0(t1)
	lw	t3,0(a7)
	lw	a4,0(a6)
	sub	a5,a5,s0
	snez	a5,a5
	neg	a5,a5
	addi	t4,t3,-6
	andi	a5,a5,-6
	addi	a4,a4,-2
	max	a4,a4,t4
	addi	a5,a5,2
	addi	a3,a3,-6
	addi	a1,a1,-2
	add	a5,a5,t5
	max	t4,a4,zero
	max	a1,a1,a3
	max	a5,a5,t4
	max	a3,a5,a1
	sw	a4,0(a6)
	sw	a3,0(a7)
	addi	t1,t1,1
	max	a0,a0,a3
	addi	a7,a7,4
	addi	a6,a6,4
	bne	t6,t1,.L12
	addi	t0,t0,1
	bne	t0,t2,.L8
	lw	s0,12(sp)
	.cfi_restore 8
	addi	sp,sp,16
	.cfi_def_cfa_offset 0
	jr	ra
	.cfi_endproc
.LFE1:
	.size	sw_gotoh, .-sw_gotoh
	.bss
	.align	2
	.type	E.0, @object
	.size	E.0, 16388
E.0:
	.zero	16388
	.type	H.1, @object
	.size	H.1, 16388
H.1:
	.zero	16388
	.ident	"GCC: (Debian 16.2.0-3) 16.2.0"
	.section	.note.GNU-stack,"",@progbits
