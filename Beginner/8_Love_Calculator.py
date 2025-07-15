def calculate_love_score(name_1, name_2):
    true_word = "true"
    true_total = []
    love_word = "love"
    love_total = []
    for letter in true_word:
        count_1 = name_1.count(letter)
        count_2 = name_2.count(letter)
        total_count = count_1 + count_2
        true_total.append(total_count)
    true_total = sum(true_total)

    for letter in love_word:
        count_1 = name_1.count(letter)
        count_2 = name_2.count(letter)
        total_count = count_1 + count_2
        love_total.append(total_count)
    love_total = sum(love_total)
    love_score = str(true_total) + str(love_total)
    print(love_score)

calculate_love_score("Kanye West", "Kim Kardashian")
