from lab_5.groundhog_day import groundhog_day
from lab_5.gears import gears
from lab_5.brackets import brackets



def main():
    data = ['Groundhog Festival in Punxsutawney.',
            'Groundhog Festival in Punksutawney.',
            'Groundhog Festivel in Punxsutowney.']
    print(groundhog_day(data))
    data = [[0, 2, 30, 15], [14, 3, 21, 60], [7, 16, 4, 8]]
    print(gears(data, 30, 7))
    line = "[12 / (9) + 2(5{15 * <2 - 3>}6)]"
    print(brackets(line))


if __name__ == '__main__':
    main()