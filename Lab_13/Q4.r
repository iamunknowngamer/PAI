income <- 100000

if(income < 30000){
    print(paste("Final income: ",income))
    print(paste("Applicable Tax: ",0))
}else if(income >= 30000 && income < 70000){
    final <- income + income*0.1
    print(paste("Final income: ",final))
    print(paste("Applicable Tax: ",income*0.1))
}else if(income >= 70000 && income < 100000){
    final <- income + income*0.15
    print(paste("Final income: ",final))
    print(paste("Applicable Tax: ",income*0.15))
}else if(income >= 100000){
    final <- income + income*0.2
    print(paste("Final income: ",final))
    print(paste("Applicable Tax: ",income*0.2))
}
