def move(my_list, direction):
    try:
        index_of_one = my_list.index(1)
    except ValueError:
        return my_list # מחזיר את הרשימה אם 1 לא נמצא

    if direction == 'right' and index_of_one < len(my_list) - 1:
        my_list[index_of_one] = 0        # הופך את המיקום הנוכחי ל-0
        my_list[index_of_one + 1] = 1    # הופך את המיקום החדש (ימינה) ל-1

    elif direction == 'left' and index_of_one > 0:
        my_list[index_of_one] = 0        # הופך את המיקום הנוכחי ל-0
        my_list[index_of_one - 1] = 1    # הופך את המיקום החדש (שמאלה) ל-1

    return my_list
