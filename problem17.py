str1_9 = "onetwothreefourfivesixseveneightnine"
count1_9 = len(str1_9)

str10_19 = "teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen"
count10_19 = len(str10_19)

count20 = len("twenty")
count30 = len("thirty")
count40 = len("forty")
count50 = len("fifty")
count60 = len("sixty")
count70 = len("seventy")
count80 = len("eighty")
count90 = len("ninety")
count00 = len("hundred")
count1000= len("onethousand")
countAnd = 3

c1_99 = count1_9 * 9 + count10_19 + (count20 + count30 + count40 + count50 + count60 + count70 + count80 + count90) * 10
c100_999 = count1_9 * 99 + (count00 + countAnd) * 99 * 9 + c1_99 * 9 + count00 * 9 + count1_9
c1_1000 = count1000 + c100_999 + c1_99

print(c1_1000)