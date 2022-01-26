from primePy import primes

primes_10=primes.upto(10)
print("10까지의 소수 리스트: ",primes_10)
primes_100=primes.upto(100)
print("100까지의 소수 리스트: ",primes_100)
print()

first_primes_5=primes.first(5)
print("처음 5개 소수 리스트: ",first_primes_5)
first_primes_10=primes.first(10)
print("처음 10개 소수 리스트: ",first_primes_10)
print()

print("15는 소수인가요? ",primes.check(15))
print("277는 소수인가요? ",primes.check(277))
print()

prime_100_to_1000=primes.between(100,1000)
print("100부터 1000까지의 소수 리스트: ",prime_100_to_1000)