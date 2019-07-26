n_day = int(input())
n_month = int(input())
n_year = int(input())

b_day = int(input())
b_month = int(input())
b_year = int(input())


if b_year == n_year and b_month <= n_month and b_day <= n_day or b_year == n_year -1 and b_month > n_month:
    print(0)
elif  b_year <= n_year -1 and b_month <= n_month and b_day <= n_day:
    print(n_year - b_year)
elif b_year < n_year:
    print(n_year - b_year - 1)
elif b_year >= n_year and b_month >= n_month and b_day > n_day:
    print("Вы ещё не родились")