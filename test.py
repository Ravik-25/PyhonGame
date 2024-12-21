#tata cara pengunaan array data yang dari array mulainya dari 0 bukan dari 1
hobbies = ["membaca", "olahraga", "menulis" ]
tmp_hobbies = hobbies   #apapun yang ada di variabel habbies maka akan di tampung jg di dalam variabel tmp_habbies
print(f"hobbi ->>> {hobbies}")
 #misalnya mau ganti data di tmp_hobbies 
tmp_hobbies[100 - 99] = "ngoding"
print(f"tmphobbies {tmp_hobbies}")

