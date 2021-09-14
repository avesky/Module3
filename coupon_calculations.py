"""
Program: coupon_calculations.py
Author: Andy Volesky
Last date modified: 09/13/2021

The purpose of this program:

You are online shopping at SuperAwesomeCouponDealsAndStuff.com. They offer two types of discounts,
cash-off coupons and percent discount coupons. You must add tax after applying coupons.
If you have cash-off coupons, those must be applied first, then apply the percent discount coupons on the pre-tax amount.

The following is the order of calculations:

The first is cash-off coupons, that you earn by shopping. You may apply one $5 or $10 cash off per order.
The second is percent discount coupons for 10%, 15%, or 20% off.
The third is tax according to the the following guidelines:
up to $10 dollars, shipping is $5.95
$10 and up to $30 dollars, shipping is $7.95
$30 and up to $50 dollars, shipping is $11.95
Shipping is free for $50 and over

In this program, prompt the user for the the amount of the purchase, the cash coupon, the percent coupon.
Then calculate and return the total order item.
For instance, you have $5 off and 30% coupons and your item is $15.99, you will first take
$15.99 - $5.00 = $10.99.
30% off $10.99 to get $7.69
Add tax at 6% to get $8.15
Add shipping cost before tax $5.95 to get $14.10
Do not forget to use variables and constants where appropriate. Using variaables, the first line might look like the following:
cash_off_subtotal = price - cash_off
"""

import constants

#enter Purchase amount
purchase_amount = float(input('How much is your purchase? '))

#deduct cash-off
cash_off = float(input('How much is your Cash Discount ($5 or $10? $'))

cash_off_subtotal = purchase_amount - cash_off

#deduct percent discount
percent_off = float(input('What is your percentage discount? (10, 15, or 20)? '))
decimal_conversion = 1 - (percent_off*.01)

percent_off_subtotal = cash_off_subtotal*decimal_conversion

#calculate total including tax
tax_calc = percent_off_subtotal*(constants.TAX+1)

#add shipping to post-discount, pre-tax total
if percent_off_subtotal < 10:
    shipping_cost = 5.95
elif 10 <= percent_off_subtotal < 30:
    shipping_cost = 7.95
elif 30 <= percent_off_subtotal < 50:
    shipping_cost = 11.95
elif percent_off_subtotal >= 50:
    shipping_cost = 0

#calculate final total with discounts, tax, and shipping applied.

final_total = tax_calc + shipping_cost

#keep 2 digits after decimal.
final_total = format(final_total, '.2f')

print(f'Your total price including all discounts, tax and shipping is ${final_total}.  Thanks for giving us money!')


