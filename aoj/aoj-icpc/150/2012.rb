loop {
	e = m = gets.to_i
	break if e == 0
	loop.with_index { |_, z|
		break if z**3 > e
		y = Math.sqrt(e-z**3).to_i
		m = [m,e+y+z-y**2-z**3].min
	}
	puts m
}

