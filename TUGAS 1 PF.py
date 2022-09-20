### NOMOR 1 
sum_square = [1,2,3]
xs = []
for i in sum_square:
    xs.append(i*i)

def sum(xs):
    sum=0
    for i in xs:
        sum=sum+ i
    return sum
print(sum(xs))


## NOMOR 2
num = int(input("masukkan angka triangular: "))
def triangular(num) :
    sum = 0
    for i in range(1, num+1) :
        sum = sum + i
    return sum
hasil = triangular(num)
print("Hasil:", hasil ) 


# ## NOMOR 3
bil = int(input('Masukkan bilangan: '))
quad = int(input('Masukkan pangkat: '))

def fungsi_pangkat(bil,quad):
    if quad > 1:
        return bil * fungsi_pangkat(bil,quad - 1)
    return bil

hasil = fungsi_pangkat(bil, quad)
print(f'Hasil = {hasil}')


## NOMOR 4
def palindrome(s):
    return s==s[::1]

s = 'kayak'
ans = palindrome(s)

if ans:
    print('YES')
else:
    print('NO')