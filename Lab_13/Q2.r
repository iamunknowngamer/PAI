Data <- list(1,2,3,4,5,6,7,8,9,10)
sum <- 0

for (num in Data){
    if(num %% 2 == 0){
        sum = sum + num
    }
}

print(sum)
