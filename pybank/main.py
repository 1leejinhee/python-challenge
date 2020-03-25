with open("pybank_data.csv") as pybank_data_file:
    profit_losses = []
    profit_loss_changes = []
    max_inc_date = None
    max_dec_date = None
    prev_profit_loss = 0
    line_num = 0
    lines = pybank_data_file.readlines()
    for line in lines:
        if line_num > 0:
            cols = line.split(',')
            date = cols[0]
            profit_loss = int(cols[1])
            profit_loss_change = profit_loss - prev_profit_loss

            profit_losses.append(profit_loss)
            profit_loss_changes.append(profit_loss_change)
            prev_profit_loss = profit_loss

            if profit_loss_change >= max(profit_loss_changes):
                max_inc_date = date
            if profit_loss_change <= min(profit_loss_changes):
                max_dec_date = date

        line_num += 1

    print('Total Months:', len(profit_losses))
    print(f'Total: ${sum(profit_losses)}')
    print(f'Average Change: ${sum(profit_loss_changes) / len(profit_losses)}')
    print(f'Greatest Increase in Profits: {max_inc_date} ${max(profit_loss_changes)}')
    print(f'Greatest Decrase: {max_dec_date} ${min(profit_loss_changes)}')

    with open('analysis.txt', 'w') as analysis:
        print('Financial Analysis',  file=analysis)
        print('--------------------------',  file=analysis)
        print('Total Months:', len(profit_losses), file=analysis)
        print(f'Total: ${sum(profit_losses)}', file=analysis)
        print(f'Average Change: ${sum(profit_loss_changes) / len(profit_losses)}', file=analysis)
        print(f'Greatest Increase in Profits: {max_inc_date} ${max(profit_loss_changes)}', file=analysis)
        print(f'Greatest Decrease: {max_dec_date} ${min(profit_loss_changes)}', file=analysis)
