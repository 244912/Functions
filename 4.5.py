def pts_to_grade(points):
    if points >= 18:
        return "Excellent"    
    if points >= 14:
        return "Good"          
    if points >= 10:
        return "Satisfactory" 
    return "Fail"              

test_result = 15

final_grade = pts_to_grade(test_result)

print("Zdobyłeś", test_result, "punktów. Twoja ocena:", final_grade)