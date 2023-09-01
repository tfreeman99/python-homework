## Initial

import pandas as pd

df = pd.read_csv("C:\\Users\\tfree\\Desktop\\MIA Fintech bc\\MIA-VIRT-FIN-PT-08-2023-U-LOLC\\02-Python\\Homework Instructions\\PyBank\\Resources\\budget_data.csv") 

df.head(10)

## Total number of months included in a dataset

total_months = df['Date'].nunique()
print("Total Months:", total_months)

## The net total amount of Profit/Losses over the entire period

net_total = df['Profit/Losses'].sum()
print("Total:",'$' net_total)

## The average of the changes in Profit/Losses over the entire period.

df['Difference'] = df['Profit/Losses'].diff()
average_change = df['Difference'].mean()
formatted_average_change = "${:,.2f}" .format(average_change)
print("Average change:", formatted_average_change)

## The greatest increase in profits

df['Difference'] = df['Profit/Losses'].diff()
max_increase = df['Difference'].max()
formatted_max_increase = "(${:.0f})".format(max_increase)
date_of_max_increase = df.loc[df['Difference'] == max_increase, 'Date'].values[0]
print("Greatest increase in profits:", date_of_max_increase , formatted_max_increase)

## The Greatest decrease in profits

df['Difference'] = df['Profit/Losses'].diff()
max_decrease = df['Difference'].min()
formatted_max_decrease = "(${:.0f})".format(max_decrease)
date_of_max_decrease = df.loc[df['Difference'] == max_decrease, 'Date'].values[0]
print("Greatest decrease in profits:", date_of_max_decrease , formatted_max_decrease)

files_output = Path("analysis/budget_analysis.txt")
with open(files_output, 'w') as txt_file:

    txt_file.write(f'Financial Analysis\n')
    txt_file.write(f"---------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${net_total}\n")
    txt_file.write(f"Average change: {formatted_average_change}\n")
    txt_file.write(f"Greatest increase in profits: {date_of_max_increase} {formatted_max_increase}\n")
    txt_file.write(f"Greatest decrease in profits: {date_of_max_decrease} {formatted_max_decrease}\n")
