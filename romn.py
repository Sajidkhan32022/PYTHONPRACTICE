# Input Parameter: a decimal value n
# Return Value: a string containing the Roman numeral representation of n
def roman(n):
    tenplace=['','x','xx','xxx']
    oneplace=['','I','II','III','IV','V','VI','VII','VIII','IX','X']
    oneplaceindex=n%10
    tenplaceindex=n//10
    x=oneplace[oneplaceindex]
    y=tenplace[tenplaceindex]

    return y+x



pass
if __name__ == "__main__":
    for i in range(1,4039):
        if i % 5 == 0:
            print()

        print(i, roman(i), ", ", end="")
