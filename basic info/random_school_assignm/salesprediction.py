#Sales Prediction, user is already logged in, and now has accessed the sales
#prediction app, they are currently seeing the total amount of sales from their
#recent sale


#Give user input to type how many units of products have been sold
projected_amount_of_sales = float(input('How many units have been sold as of' + '\n'
                                  + 'late annual sales update? '))


#Message update from Sale Admin
print('\n' + 'UPDATE: Sale Admin -to all: Good morning team, as of late we currently'
      + '\n' + 'determine that our annual profit is at 23% in total sales!' +
      '\n' + 'Please make sure to update your total sales percentage report with 23%'
             ' for our annual report!' + '\n' + 'Thanks! ' + '\n')

#Calculating annual percentage / also allow user to update the sale percentage report
annual_percentage = float(input('Enter Updated total sale percentage report: '))

#Profit margin from  projected_amount_of_sales alger. the annual_percentage with
#annual being yearly '1'
profit_margin = (projected_amount_of_sales * annual_percentage)

#print profit report
print('Our profit for this annual report is: $' + str(profit_margin) + ' ' + 'dollars')
