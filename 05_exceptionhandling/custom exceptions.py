#You created your own exception.
''' class InsufficientBalanceError(Exception):
    pass'''


balance = 1000

amount = int(input())

if amount > balance:

    raise InsufficientBalanceError(
        "Not enough balance" )