# Есть строка с перечислением песен
# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.
## 0 1 2 3 4 5 6789 10111213141516171819202122  
## W a s t e  a  M o m e n t  S t a y i n g \ ' A l i v e  A  S o r t a  F a i r y t a l e  S t a r t  M e  U p  N e w  S a l v a t i o n  

my_favorite_songs_lst = 'Waste a Moment Staying\' Alive A Sorta Fairytale Start Me Up New Salvation'
print((my_favorite_songs_lst[0:14]), (my_favorite_songs_lst[-14:]), (my_favorite_songs_lst[15:30]), (my_favorite_songs_lst[-26:-14]))
