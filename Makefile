
all:
	@gcc -Wall create_mseed.c -o create_mseed

clean:
	@rm create_mseed
