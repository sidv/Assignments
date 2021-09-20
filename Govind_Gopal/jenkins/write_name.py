#  GNU nano 4.8                                                             write_name.py                                                                        
fd = open("new_file","x")
fd.close()
fd = open("new_file","w")
text = "My name is Govind Gopal"
fd.write(text)
fd.close()


