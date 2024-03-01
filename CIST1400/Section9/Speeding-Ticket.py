def calculate_reward(speed, limit):

   difference = limit - speed  

   if difference >= 10:
       reward = 50  
   elif  6 <= difference <= 20:
       reward = 75  
   elif 21 >= difference <= 40:
       reward = 150 
   elif difference > 40:
       reward = 300  
   else:
       reward = 0  

   return reward

limit = float(input())
speed = float(input())


reward = calculate_reward(speed, limit)

print(reward)
