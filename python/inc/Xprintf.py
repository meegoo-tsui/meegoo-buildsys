#! /usr/bin/python

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    Xprintf.py
#  @brief   printf message with color.
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @package Xprintf
#  @brief   printf message with color.
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/04

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## color reset
txtrst = "\033[1;m"
## color red
txtred = "\033[1;31m"
## color green
txtgrn = "\033[1;32m"
## color yellow
txtylw = "\033[1;33m"
## color blue
txtblu = "\033[1;34m"
## color purple
txtpur = "\033[1;35m"
## color cyan
txtcyn = "\033[1;36m"
## color white
txtwht = "\033[1;37m"
## color list
color_list = [txtrst, txtred, txtgrn, txtylw, txtblu, txtpur, txtcyn, txtwht]
## Printf message with colors.
class printf:
	## Printf message.
	#  @param color int
	#  @param message string
	def printf(self, color, message):
		if color > 7 or color < 0:
			color = 0
		print color_list[color] + message + color_list[0]
		return

	## printf test info.
	def test(self):
		self.printf(0, "color 0 - message...")
		self.printf(1, "color 1 - message...")
		self.printf(2, "color 2 - message...")
		self.printf(3, "color 3 - message...")
		self.printf(4, "color 4 - message...")
		self.printf(5, "color 5 - message...")
		self.printf(6, "color 6 - message...")
		self.printf(7, "color 7 - message...")
		return

	## printf error info then exit.
	def error(self, message):
		self.printf(1, "<error>\n\t" + message)
		sys.exit(1)

	## printf status info.
	def status(self, message):
		self.printf(4, "<status>\n\t" + message)
		return

	## reset the termenal
	def reset(self):
		os.system("echo -e \\\\033c")
		return


## object of class printf
printf = printf()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## Test printf package.
def main():
	printf.reset()
	printf.status("Test package printf ...")
	printf.test()
	printf.status("Test package printf ok.")

	sys.exit(0)

if __name__ == '__main__':
	main()

