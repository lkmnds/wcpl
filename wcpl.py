#!/usr/bin/env python3

import sys
argv = sys.argv

WCPL_VERSION = '0.0.1'
WCPL_BUILD = 2

def wcpl(data, env):
	compiled = []
	env['_head'] = ''

	for line in data.split('\n'):
		if len(line) < 1:
			continue
		cmd = line[0]
		commands = line.split(' ')
		if commands[0] == 'm':
			meta_type = commands[1]

			# m <type> <var>=<val>
			# val = l(type) + 1 + l(var) + 1
			meta_command = (''.join(commands[2:])).split('=')
			meta_var = meta_command[0]
			meta_val = meta_command[1]

			if meta_type == 's':
				# read string
				# meta_val = meta_val[1:-1]
				env['meta'][meta_var] = meta_val
			elif meta_type == 'r':
				env['meta'][meta_var] = meta_val

			env['_head'] += '<meta %s=%s>' % (meta_var, meta_val)
		elif commands[0] == '0':
			compiled.append("<p>%s</p>" % ' '.join(commands[1:]))
		elif commands[0] == 'l':
			text = commands[1]
			linkv = commands[2]
			compiled.append("<a href=\"%s\">%s</a>" % (linkv, text))

		# elif commands[0] == ''

	res = ''

	res += '<head>\n %s \n</head>\n' % ''.join(env['_head'])
	res += '\n<body>\n %s \n</body>' % '\n'.join(compiled)

	return '<html>\n%s\n</html>' % res

def main():
	if len(argv) > 1:
		fname = argv[1]
		result = ""
		env = {
			"meta": {
				"charset": "utf-8",
			},
			"wcpl": {
				"version": WCPL_VERSION,
				"build": WCPL_BUILD,
			}
		}
		with open(fname, 'r') as f:
			print(wcpl(f.read(), env))

if __name__ == '__main__':
	main()
