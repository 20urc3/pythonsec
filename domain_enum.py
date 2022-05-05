import sublist3r

domains = open("domains.txt", "r")
domains2 = open("domains_found.txt","w")

for domain in domains.readlines():
	domains2.write(domain.lstrip('www.'))

domains=open("domains_found.txt", "r")
for domain in domains.readlines():
	domain = domain.rstrip("\n")
	subdomains = sublist3r.main(domain, 40,	domain+'_subdomains.txt', silent=True, engines=None, enable_bruteforce=False, verbose=False, ports =None)

for sub in subdomains:
	print(sub)
