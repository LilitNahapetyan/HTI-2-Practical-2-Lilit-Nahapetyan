def roman_to_integer(rom):
    dict_rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if len(rom) == 1:
        return dict_rom[rom[0]]

    sum_el = 0
    i = 0
    while i < (len(rom) - 1):
        if dict_rom[rom[i]] < dict_rom[rom[i + 1]]:
            sum_el += dict_rom[rom[i + 1]] - dict_rom[rom[i]]
            i += 2
        else:
            sum_el += dict_rom[rom[i]]
            i += 1

    if dict_rom[rom[-1]] <= dict_rom[rom[-2]]:
            sum_el += dict_rom[rom[-1]]

    return sum_el

rom_num = input("Input Roman Number: ").upper()
print(roman_to_integer(rom_num))

