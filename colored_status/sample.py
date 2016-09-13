#!/usr/bin/python

import coloredstatus as cs

cs.print_status("Scanning...")
#print cs.status + "Scanning..."
cs.print_good("Found service on port 21")
cs.print_error("Failed to find service!")
cs.print_warning("This action might potentially be harmful!")
cs.print_money("Shadow file dumped!")
cs.print_special("Root access gained!")
