#!/usr/bin/env ruby
# Regular expression to parse a log file

puts ARGV[0].scan(/from:(\+?\d+|\w+),to:(\+?\d+|\w+),flags:([-,\d:]+)/).join
