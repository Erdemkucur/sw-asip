	.file	"rv_kernel.c"
	.option pic
	.attribute arch, "rv32i2p1_m2p0_zmmul1p0"
	.attribute unaligned_access, 0
	.attribute stack_align, 16
	.text
	.align	2
	.globl	sw_gotoh
	.type	sw_gotoh, @function
sw_gotoh:
.LFB1:
	.cfi_startproc
	addi	sp,sp,-16
	.cfi_def_cfa_offset 16
	sw	s0,12(sp)
	.cfi_offset 8, -4
	mv	s0,a2
	blt	a3,zero,.L2
	lla	a5,H.1+4
	slli	a6,a3,2
	li	a2,-999424
	add	a6,a6,a5
	addi	a2,a2,-576
	lla	a5,H.1
	lla	a4,E.0
.L3:
	sw	zero,0(a5)
	sw	a2,0(a4)
	addi	a5,a5,4
	addi	a4,a4,4
	bne	a5,a6,.L3
.L2:
	ble	a1,zero,.L4
	mv	t2,a0
	add	a2,a0,a1
.L5:
	bgt	a3,zero,.L25
	addi	t2,t2,1
	bne	t2,a2,.L5
.L4:
	lw	s0,12(sp)
	.cfi_remember_state
	.cfi_restore 8
	li	a0,0
	addi	sp,sp,16
	.cfi_def_cfa_offset 0
	jr	ra
.L25:
	.cfi_restore_state
	add	t0,s0,a3
	li	a0,0
.L14:
	lbu	t6,0(t2)
	li	a1,-999424
	addi	a1,a1,-576
	mv	t1,s0
	lla	a7,H.1+4
	lla	a6,E.0+4
	li	a5,0
	li	t5,0
.L13:
	lbu	a4,0(t1)
	lw	t4,0(a7)
	lw	a3,0(a6)
	sub	a4,a4,t6
	snez	a4,a4
	neg	a4,a4
	andi	a4,a4,-6
	addi	t3,t4,-6
	addi	a3,a3,-2
	addi	a4,a4,2
	bge	a3,t3,.L7
	mv	a3,t3
.L7:
	sw	a3,0(a6)
	addi	a5,a5,-6
	addi	a1,a1,-2
	bge	a1,a5,.L8
	mv	a1,a5
.L8:
	not	t3,a3
	srai	t3,t3,31
	add	a5,a4,t5
	and	a3,a3,t3
	bge	a5,a3,.L10
	mv	a5,a3
.L10:
	bge	a5,a1,.L11
	mv	a5,a1
.L11:
	sw	a5,0(a7)
	bge	a0,a5,.L12
	mv	a0,a5
.L12:
	addi	t1,t1,1
	addi	a7,a7,4
	addi	a6,a6,4
	beq	t0,t1,.L26
	mv	t5,t4
	j	.L13
.L26:
	addi	t2,t2,1
	bne	t2,a2,.L14
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
