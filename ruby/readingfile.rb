# print "What's the file name? "
# filename = gets.chomp

# Reading a file
#puts open("filename").read

#wriring in a file
# file=open("capitalizeandreverse.rb",'w')
# file.write("\n my name is shubham")

#copying a file
file1=open("capitalizeandreverse.rb").read

file2=open("newfile.rb",'w')

file2.write(file1)

file2.close
