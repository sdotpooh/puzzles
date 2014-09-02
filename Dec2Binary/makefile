main = dec2bin
mainans = dec2bin_ans
CC = g++
CFLAGS = -Wall -std=c++0x

$(main) : $(main).cpp
	$(CC) $(CFLAGS) $< -o $@

$(mainans) : $(mainans).cpp
	$(CC) $(CFLAGS) $< -o $@

.PHONY : ans
ans : $(mainans)
	mv $(mainans) $(main)

.PHONY : clean
clean :
	rm -f $(main) $(mainans)


