def vyvod(num1, stepen):
    chtoto = num1
    chtoto1 = 1 / num1
    if stepen > 0:
        for i in range(stepen - 1):
            chtoto = chtoto * num1
        return chtoto
    elif stepen == 0:
        return 1
    else:
        for i in range(-stepen - 1):
            chtoto1 = chtoto1 * (1 / num1)
        return chtoto1


print(vyvod(2,-2))