person = { name: "Mattan", age: 28, height: 5 * 12 + 10 }
puts person[:name]

person.each do |key, value|
  puts "The key is: #{key} \nand the value is: #{value}\n\n"
end