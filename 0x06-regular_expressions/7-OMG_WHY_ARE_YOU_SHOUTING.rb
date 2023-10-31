#!/usr/bin/env ruby
# Regular expression to match only capital letter

puts ARGV[0].scan(/[A-Z]/).join
