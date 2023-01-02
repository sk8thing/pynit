def to_units(x_,  offset=0, decimals=2, suffix=""):
    units = {-12: "T",-9: "G",-6: "M",-3: "K",0: "",3: "m",6: "µ",9: "n",12: "p",15: "f"}
    k = -12
    while x_ * 10.0**k < 1:
        k += 3
    return f"{str(round(x_*10.0**k, decimals)).ljust(2 + decimals, '0')}{units[k + offset]}{suffix}"