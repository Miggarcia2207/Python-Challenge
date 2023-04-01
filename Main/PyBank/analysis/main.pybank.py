#PyBank
import csv

def read_csv_file(file_path):
    
    with open(file_path) as file:
        reader = csv.reader(file)
        return list(reader)

def parse_data(data):
    
    total_months = 0
    total_profit_loss = 0
    previous_profit_loss = None
    profit_loss_changes = []
    months = []

    for row in data:
        if row[0] == "Date":
            continue

        total_months += 1

        total_profit_loss += int(row[1])

        current_profit_loss = int(row[1])
        if previous_profit_loss is not None:
            profit_loss_changes.append(current_profit_loss - previous_profit_loss)

        months.append((row[0], current_profit_loss))

        previous_profit_loss = current_profit_loss

    return total_months, total_profit_loss, profit_loss_changes, months


def calculate_analysis(total_months, total_profit_loss, profit_loss_changes, months):
   
    average_change = sum(profit_loss_changes) / len(profit_loss_changes)
    greatest_increase = max(profit_loss_changes)
    greatest_decrease = min(profit_loss_changes)

    greatest_increase_month = None
    greatest_increase_amount = None
    greatest_decrease_month = None
    greatest_decrease_amount = None

    for month, change in months:
        if change == greatest_increase:
            greatest_increase_month = month
            greatest_increase_amount = change
        elif change == greatest_decrease:
            greatest_decrease_month = month
            greatest_decrease_amount = change

    return {
        "Total Months": total_months,
        "Total": total_profit_loss,
        "Average Change": average_change,
        "Greatest Increase in Profits": f"{greatest_increase_month} (${greatest_increase})",
        "Greatest Decrease in Profits": f"{greatest_decrease_month} (${greatest_decrease})"
    }


def print_analysis(analysis):
    
    print("Financial Analysis")
    print("----------------------------")
    for key, value in analysis.items():
        print(f"{key}: {value}")


def main(file_path):
    
    data = read_csv_file(file_path)
    total_months, total_profit_loss, profit_loss_changes, months = parse_data(data)
    analysis = calculate_analysis(total_months, total_profit_loss, profit_loss_changes, months)
    print_analysis(analysis)


if __name__ == "__main__":
    main("budget_data.csv")
