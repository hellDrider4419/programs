def multiply(a,b)
	puts "multiplying #{a} and #{b}"
	return a*b
end

def add(a,b)
	puts "adding #{a} and #{b}"
	return a+b
end

def subtract(a,b)
	puts "subtracting #{a} and #{b}"
	return a-b
end

def divide(a,b)
	puts "dividing #{a} and #{b}"
	return b/a
end


a= add(10,20)
puts "#{a}"
a= multiply(10,20)
puts "#{a}"
a= subtract(10,20)
puts "#{a}"
a= divide(10,20)
puts "#{a}"