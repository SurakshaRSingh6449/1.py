

import datetime as dt

#printing the present datetime
print(dt.datetime.now())

def even_numbers():
    
    #creating the list of dictionaries
    numbers = [{'sequence': '951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527'}]
    
    #Now spliting the values 
    for i in numbers[0].values():
        new_list =list((i.split(',')))
    
    #converting the values to integer 
    new_list2 = list(int(a) for a in new_list)
    
    #finally following the even number operation
    for x in new_list2:
        if x%2==0:
            print(x)
        
#calling the even_numbers function
even_numbers()