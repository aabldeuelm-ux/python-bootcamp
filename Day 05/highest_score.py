student_scores = [150, 185, 130,126, 189, 157, 146, 137, 140, 140]
fruits = ["Apple","Mangoes","Bananana","Orange"]
total_score = sum(student_scores)
# print(total_score)
# sum = 0
# for score in student_scores:
#     sum += score
# print(min(student_scores)) # shows the least number from the list of student_scores
# print(max(fruits)) # gives the highest or maximum string based on the alphabets....a > A and the more the order of the alphabet the more value they hold like z > a

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)