
def log_operation(f):
    def wrapper(*args):
        try:
            print("Starting withdraw...")
            res = f(*args)
            print("Withdrawal successful.")
            return res
        except Exception as e :
            print(f"ERROR: {e}")
            return None
        
    return wrapper


@log_operation
def withdraw(balance , amount):
    
    if isinstance(amount , bool) or not isinstance(amount,(int , float)):
        raise TypeError("Amount must be a number")
    if amount <= 0:
        raise ValueError("Amount must be greater than zero !! ")
    if amount > balance:
        raise ValueError("Insufficient balance !!")

    
    return balance-amount

res = withdraw(5,True)
print(res)
