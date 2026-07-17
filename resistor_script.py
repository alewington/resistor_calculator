# python
# Version 0.1
# resistor calculator


band_Types = [
    ["Black", 0, 1, 0, 250],
    ["Brown", 1, 10, 1, 100],
    ["Red", 2, 100, 2, 50],
    ["Orange", 3, 1000, 0, 15],
    ["Yellow", 4, 10000, 0, 25],
    ["Green", 5, 100000, 0.5, 20],
    ["Blue", 6, 1000000, 0.25, 10],
    ["violet", 7, 10000000, 0.1, 5],
    ["Grey", 8, 100000000, 0.05, 1],
    ["White", 9, 1000000000, 0, 0],
    ["Gold", 0, 0.1, 5, 0],
    ["Silver", 0, 0.01, 10, 0],
    ["No Band", 0, 0, 20, 0]
]

band_checker = [
    ["Black", 1, 1, 1, 1, 0, 1],
    ["Brown", 1, 1, 1, 1, 1, 1],
    ["Red", 1, 1, 1, 1, 1, 1],
    ["Orange", 1, 1, 1, 1, 0, 1],
    ["Yellow", 1, 1, 1, 1, 0, 1],
    ["Green", 1, 1, 1, 1, 1, 1],
    ["Blue", 1, 1, 1, 1, 1, 1],
    ["violet", 1, 1, 1, 0, 1, 1],
    ["Grey", 1, 1, 1, 1, 0, 1],
    ["White", 1, 1, 1, 0, 0, 0],
    ["Gold", 0, 0, 0, 1, 1, 0],
    ["Silver", 0, 0, 0, 1, 1, 0],
    ["No Band", 0, 0, 0, 1, 0, 0]
]


band_Select = []

# menu
"""
def main():
    while True:
        print("Resistor Calculator")
        print("1. Select Bands")
        print("2. Find Resistor Value")
        print("3. Reset Bands")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            select_bands()
        elif choice == "2":
            find_resistor_value()
        elif choice == "3":
            reset_bands()
        elif choice == "4":
            break
        else:
            print("Invalid choice,  please try again.")
"""


def band_Selection():
    band_Choice = int(input("select band:"))
    return band_Choice


def resistor_Selection():
    bands_No = int(input("select number of bands:"))
    return bands_No


def list_Resistors():
    print(("-"*20)*6)
    txt = (f"{0:^20}|{1:^20}|{2:^20}|{3:^20}|{4:^20}|{5:^20}|{6:^20}")
    print(txt.format(
        "Colour",
        "1st Band",
        "2nd Band",
        "3rd Band",
        "Multiplier",
        "Tolerence",
        "Temp Coefficent"
        ))
    print(("-"*20)*6)
    for x in band_Types:
        print(f"{x[0]:^20}",
              f"|{x[1]:^20}",
              f"|{x[1]:^20}",
              f"|{x[1]:^20}",
              f"|{x[2]:^20}",
              f"|{x[3]:^20}",
              f"|{x[4]:^20}"
              )


def list_Band():
    # list bands to select from,  then select bands and assign to variables
    # for calculation,  then calculate and output result.
    print("Band List:")
    for i in band_Types:
        print(f"{band_Types.index(i)+1}: {i[0]}")
    return


# append
def append_Band(band_Choice):
    band_Select.append(band_Choice-1)
    print(band_Select)
    return band_Select


# pop
def pop_Band():
    band_Select.pop(-1)
    print("Last selected band removed.")
    print(band_Select)
    return band_Select


# check
def check_Band(band_Choice):
    if band_checker[band_Choice-1][len(band_Select)] == 0:
        print(band_checker[band_Choice-1][len(band_Select)])
        print("Invalid band selection for current number of bands selected.\n",
              "Please select a different band.")
        pop_Band()
        return


# calculate
def calculate_Resistor():
    resistor_Select = resistor_Selection()
    while len(band_Select) < resistor_Select:
        band_Choice = input("Enter your choice: ")
        res = band_Choice.isdigit()
        if res:
            append_Band(int(band_Choice))
            check_Band(int(band_Choice))
            continue
        elif band_Choice == "p":
            pop_Band()
            continue
        elif band_Choice == "c":
            list_Band()
            continue
        elif band_Choice == "r":
            band_Select.clear()
            print("Bands reset.")
            print(band_Select)
            continue
        elif band_Choice == "e":
            exit()
            return
        else:
            print("Invalid choice,  please try again.")
    return band_Select


def band_Output():
    print("Selected Bands:")
    band_Outlist = []
    for i in band_Select:
        band_Outlist.append(band_Types[i][0])

    for i in band_Outlist:
        print(f"Band Colour {band_Outlist.index(i)+1:<2}: {i:<2}",  end=" | ")
    print("")


def si_Unit(resistor_Value):
    if resistor_Value >= 1000000000:
        resistor_Value_SI = resistor_Value / 1000000000
        print(
            f"Resistor Value: {resistor_Value_SI} GΩ (SI Unit - convertion",
            "to a higher Si Prefix)"
            )
    elif resistor_Value >= 1000000:
        resistor_Value_SI = resistor_Value / 1000000
        print(
            f"Resistor Value: {resistor_Value_SI} MΩ (SI Unit - convertion",
            "to a higher Si Prefix)"
            )
    elif resistor_Value >= 1000:
        resistor_Value_SI = resistor_Value / 1000
        print(
            f"Resistor Value: {resistor_Value_SI} kΩ (SI Unit - convertion",
            "to a higher Si Prefix)"
            )
    else:
        print(
            f"Resistor Value: {resistor_Value} Ω (SI Unit - no conversion",
            "needed)"
            )


# start of calculation. data collation and organisation.
def band_Calculator_Setup():
    band_Multiplier = band_Types[band_Select[0]][1]
    band_Tolerence = band_Types[band_Select[1]][1]
    band_Coefficent = band_Types[band_Select[2]][1]
    return band_Multiplier,  band_Tolerence,  band_Coefficent


def band_Calculator():
    band_Multiplier, band_Tolerence, band_Coefficent = band_Calculator_Setup()
    band_Value = (
                (band_Types[band_Select[0]][1]*100)
                + (band_Types[band_Select[1]][1]*10)
                + (band_Types[band_Select[2]][1])
                )
    resistor_Value = band_Value * band_Multiplier
    return resistor_Value,  band_Tolerence,  band_Coefficent


def band_Calculator_Differential():
    resistor_Value,  band_Tolerence,  band_Coefficent = band_Calculator()
    rvbt = resistor_Value * (band_Tolerence / 100)
    resistor_Value_Max = resistor_Value + (rvbt)
    resistor_Value_Min = resistor_Value - (rvbt)
    print(f"Resistor Value: {resistor_Value} ohms",
          f"Tolerence: {band_Tolerence}%",
          f"Coefficent: {band_Coefficent}ppm/K",
          f"Max Value: {resistor_Value_Max} ohms",
          f"Min Value: {resistor_Value_Min} ohms"
          )
    si_Unit(resistor_Value)


def main():
    calculate_Resistor()
    band_Output()
    band_Calculator_Differential()


if __name__ == "__main__":
    main()
