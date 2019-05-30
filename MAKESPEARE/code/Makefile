CC=gcc
LUAJITDIR=../../LuaJIT-2.1.0-beta3

all: makespeare-x86-64 makespeare-tis100

makespeare-x86-64: search-dahc.c
	$(CC) -m64 -O3 -std=gnu99 -I$(LUAJITDIR) -I ./x86-64 -o makespeare-x86-64 search-dahc.c -lm

makespeare-tis100: search-dahc.c
	$(CC) -m64 -O3 -std=gnu99 -I$(LUAJITDIR) -I ./tis-100 -o makespeare-tis100 search-dahc.c -lm

