# + plus
# - minus
# / divide
# * times
# < less then
# > greater then

puts "Let's do some math!"

puts "What is the answer to life, the universe, and everything? #{30 + 20 - 8}"

puts "Is it true that 5 * 2 > 5 / 2"

puts 5 * 2 > 5.0 / 2

puts "What is 5 * 2? #{5 * 2}"
puts "What is 5 / 2? #{5.0 / 2}"



# Strings are text surrounded by quotes
# Both single ('') and double ("") are used
# examples: "dinosaurs", '2112', "I'm lovin' it!"

kanye_quote = "My greatest pain in life
is that I will never be able
to see myself perform live."               

hamilton_quote = "Well, the word got around, they said, \"This kid's insane, man\"" # That's how you escape text

puts hamilton_quote
puts kanye_quote




print "What's you're name? "
name = gets.chomp

print "How old are you? "
age = gets.chomp.to_i
age_in_dog_years = age / 7

puts "#{name}, your #{age_in_dog_years} in dog years. Woof!"
