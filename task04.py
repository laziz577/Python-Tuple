from typing import List,Tuple

def filter_olders(orders:List([Tuple])  List[Tuple]):
    """Filter qiluvchi funciton
    Bu function orderlarni id buyicha filter qialdi
    
    Args:
        orders(List[Tuple]): orderlar ruyxati
        
    Returns:
        List[Tuple]: filterlangan orderlar    
        """
result = list()

for order in orders:
    if order [0] % 2 == 0:
        result.append(order)
        
orders = [(102, "Ali"), (99, "Vali"), (150, "Sami")]
even_orders = filter_olders(orders)
print(even_orders)
