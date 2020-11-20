import json

with open("lesson_5-7_dd.json", "w", encoding="utf-8") as final_json:
    with open("text_7.txt", encoding="utf-8") as firm_info:
        profit, avg = {}, {}
        result = [profit, avg]
        count = 0
        avg_sum = 0
        for line in firm_info:
            key_1, value_1 = line.split()[0], int(line.split()[2]) - int(line.split()[3])
            profit[key_1] = value_1
            print(f"Прибыль компании {line.split()[1]} '{key_1}': {value_1}")
            if profit[key_1] > 0:
                avg_sum += value_1
                count += 1
            key_2, value_2 = "average_profit", avg_sum/count
            avg[key_2] = value_2
        print(f"\nСредняя прибыль всех компаний: {value_2}")

    json.dump(result, final_json, indent=4, ensure_ascii=False)
