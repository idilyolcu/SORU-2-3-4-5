histogram = {
    100: 12, 101: 18, 102: 32, 103: 48, 104: 52,
    105: 65, 106: 55, 107: 42, 108: 32, 109: 16,
    110: 10, 140: 5, 141: 18, 142: 25, 143: 32,
    144: 40, 145: 65, 146: 43, 147: 32, 148: 20,
    149: 10, 150: 4
}


T0 = 100
threshold = 1


def calculate_means(hist, threshold):
    sum_G1, sum_G2 = 0, 0
    count_G1, count_G2 = 0, 0
    for intensity, count in hist.items():
        if intensity > T0:  
            sum_G1 += intensity * count
            count_G1 += count
        else:
            sum_G2 += intensity * count
            count_G2 += count
    m1 = sum_G1 / count_G1 if count_G1 != 0 else 0
    m2 = sum_G2 / count_G2 if count_G2 != 0 else 0
    return m1, m2


while True:
    m1, m2 = calculate_means(histogram, T0)
    T1 = (m1 + m2) / 2
    if abs(T1 - T0) < threshold:
        break
    T0 = T1


print(f"Optimum eşik değeri: {T1}")
print("Yoğunluk Değeri   Piksel Sayısı")
for intensity, count in histogram.items():
    print(f"{intensity:4} {count:16}")