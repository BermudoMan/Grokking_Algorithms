def look_for_key(main_box):
	pile = main_box.make_a_pile_to_look_through()
	while pile is not empty:
		box = pile.grab_a_box()
		for item in box:
			pile.append(item)
		elif item.is_a_key():
			print("found the key!")


#recursion
def look_for_key(box):
	for item in box():
		look_for_key(item)
	elif item.is_a_key():
		print "found the key!"