import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    left_part = ''
    right_part = ''
    if re.search('to', s) == None:
        raise ValueError
    time_split = s.split(' to ')
    if re.search(" AM", time_split[0]):
        time_noam = time_split[0].replace('AM','').strip()
        if re.search(':', time_noam):
            if re.search('^1.', time_noam):
                if re.search('^12', time_noam):
                    left_part = '00:00'
                else:
                    left_part = time_noam
            else:
                time_noam_split = time_noam.split(':')
                if int(time_noam_split[0]) > 12 or int(time_noam_split[1]) >= 60:
                    raise ValueError
                left_part = str(0) + str(time_noam_split[0]) + str(':') + str(time_noam_split[1])
        else:
            if time_noam == '12':
                left_part = '00:00'
            elif time_noam in ['10','11']:
                left_part = str(time_noam) + ':00'
            else:
                left_part = str(0) + str(time_noam) + ':00'
    elif re.search(' PM', time_split[0]):
        time_nopm = time_split[0].replace('PM','').strip()
        if re.search(':', time_nopm):
            time_nopm_split = time_nopm.split(':')
            if int(time_nopm_split[0]) > 12 or int(time_nopm_split[1]) >= 60:
                raise ValueError
            number_24h = int(time_nopm_split[0]) + 12
            if number_24h == 24:
                left_part = '12:00'
            else:
                left_part = str(number_24h) + str(':') + str(time_nopm_split[1])
        else:
            if time_nopm == '12':
                left_part = '12:00'
            else:
                left_part = str(int(time_nopm) + 12) + ':00'
    else:
        raise ValueError

    if re.search(' AM',time_split[1]):
        time_noam = time_split[1].replace('AM','').strip()
        if re.search(':', time_noam):
            if re.search('^1.', time_noam):
                if re.search('^12', time_noam):
                    right_part = '00:00'
                else:
                    right_part = time_noam
            else:
                time_noam_split = time_noam.split(':')
                if int(time_noam_split[0]) > 12 or int(time_noam_split[1]) >= 60:
                    raise ValueError
                right_part = str(0) + str(time_noam_split[0]) + str(':') + str(time_noam_split[1])
        else:
            if time_noam == '12':
                right_part = '00:00'
            elif time_noam in ['10','11']:
                right_part = str(time_noam) + ':00'
            else:
                right_part = str(0) + str(time_noam) + ':00'
    elif re.search(' PM', time_split[1]):
        time_nopm = time_split[1].replace('PM','').strip()
        if re.search(':', time_nopm):
            time_nopm_split = time_nopm.split(':')
            if int(time_nopm_split[0]) > 12 or int(time_nopm_split[1]) >= 60:
                raise ValueError
            number_24h = int(time_nopm_split[0]) + 12
            if number_24h == 24:
                right_part = '12:00'
            else:
                right_part = str(number_24h) + str(':') + str(time_nopm_split[1])
        else:
            if time_nopm == '12':
                right_part = '12:00'
            else:
                right_part = str(int(time_nopm) + 12) + ':00'
    else:
        raise ValueError

    return f'{left_part} to {right_part}'

if __name__ == "__main__":
    main()
