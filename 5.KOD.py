def otsu_eşik_değeri(histogram):
    toplam = sum(histogram.values())
    sumB = 0
    wB = 0
    maksimum = 0.0
    en_uygun_eşik_değeri = 0
    sum1 = sum([i * histogram[i] for i in histogram])

    for i in range(256):  
        wB += histogram.get(i, 0)
        if wB == 0:
            continue
        wF = toplam - wB
        if wF == 0:
            break
        sumB += i * histogram.get(i, 0)
        mB = sumB / wB
        mF = (sum1 - sumB) / wF
        aradaki_fark = wB * wF * (mB - mF) ** 2
        if aradaki_fark >= maksimum:
            en_uygun_eşik_değeri = i
            maksimum = aradaki_fark

    return en_uygun_eşik_değeri


histogram = {
    100: 12, 101: 18, 102: 32, 103: 48, 104: 52, 105: 65, 106: 55, 107: 42, 108: 32, 109: 16,
    110: 10, 140: 5, 141: 18, 142: 25, 143: 32, 144: 40, 145: 65, 146: 43, 147: 32, 148: 20, 149: 10, 150: 4
}


eşik_değeri = otsu_eşik_değeri(histogram)
print("En uygun eşik değeri:", eşik_değeri)