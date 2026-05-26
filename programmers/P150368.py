def cal(users, emoticons, discounts):
    subscription_count = 0
    total_purchase_amount = 0

    for purchase_discount, upper_limit in users:
        purchase_amount = 0

        for i in range(len(emoticons)):
            if discounts[i] >= purchase_discount:
                purchase_amount += emoticons[i] * (100 - discounts[i]) // 100
            
            if purchase_amount >= upper_limit:
                break
        
        if purchase_amount >= upper_limit:
            subscription_count += 1
        else:
            total_purchase_amount += purchase_amount
    
    return subscription_count, total_purchase_amount

def recur(n, depth, users, emoticons, discounts, discounts_set):
    if n == depth:
        return cal(users, emoticons, discounts)
    
    subscription_count = 0
    total_purchase_amount = 0

    for discount in discounts_set:
        discounts.append(discount)
        count, amount = recur(n, depth + 1, users, emoticons, discounts, discounts_set)
        discounts.pop()
        
        if count > subscription_count:
            subscription_count = count
            total_purchase_amount = amount
        elif count == subscription_count and amount > total_purchase_amount:
            total_purchase_amount = amount
    
    return subscription_count, total_purchase_amount
        
def solution(users, emoticons):
    discounts_set = [10, 20, 30, 40]
    answer = recur(len(emoticons), 0, users, emoticons, [], discounts_set)
    return answer
