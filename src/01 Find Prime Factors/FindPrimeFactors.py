def get_prime_factors(val):
  result = []
  factor = 2
  valPrime = val
  while valPrime > 1:
    if valPrime % factor == 0:
      valPrime = valPrime / factor
      result.append(factor)
    else:
      factor = factor + 1
  return result

result = get_prime_factors(630)
print(result)
