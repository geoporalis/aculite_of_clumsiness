from pathlib import Path
from colorama import Fore

listOfData = []
dir = Path(__file__).parent.resolve()

# print(dir)
with open(Path(dir/'input').resolve() ,'r') as f:
    listOfData = f.readlines()

# print(listOfData[:10])
save_reports = 0
nope_reports = 0
unknown_reports = 0
for report in listOfData: #[:5]:
    report_data = [int(x) for x in report.strip('/n').split(' ')]
    report_data_diff = []
    for i in range(len(report_data)-1):
        diff = report_data[i]-report_data[i+1]
        if diff == 0 or abs(diff)> 3:
            # print(Fore.RED,'Nope', Fore.RESET, report_data) #, end=' ')
            nope_reports += 1
            report_data_diff = []
            break            
        report_data_diff.append(-1 if diff < 0 else 1)
    else:
        if report_data_diff.count(1) == len(report_data_diff) or report_data_diff.count(1) == 0:
            save_reports += 1
        else:
            # print(report_data, '\t\t', report_data_diff, '\t\t', report_data_diff.count(1), len(report_data_diff))
            nope_reports += 1
        # continue


print(Fore.GREEN, save_reports, Fore.RED, nope_reports, Fore.YELLOW, unknown_reports, Fore.RESET, save_reports+nope_reports+unknown_reports) # 3363 is to high
    # [int(X) for x in report]