def score_calculator(item_name_points, item_des_points, item_loc_points,item_img_points):
    total_score = (item_name_points + item_des_points+ item_loc_points/3 +item_img_points) / 4
    total_score = total_score*100
    return total_score
