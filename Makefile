# Makefile for source rpm: vim
# $Id$
NAME := vim
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
