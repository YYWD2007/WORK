user={"username":"efermi", "first":"enrico","last":"fermi"}            #"key":"value"
for key,value in user.items():                                         #用for循环来游历字典 
    print(f"\nKey: {key}")
    print(f"Value: {value}\n")

for key in user.keys():                                                #只游历key(.keys()可省略)
    print(key.title())



favorite_languages={                                           
                    "jen":"python",
                    "sarah":"c",
                    "edward":"rust",
                    "phil":"python",
                    }
friends=["phil","sarah"]       
for key in favorite_languages.keys():                                      
    print(f"Hi, {key.title()}.")
    if key in friends:                                                              
        language=favorite_languages[key]                               #所有的名字都被赋予了key.[]里面不写名字，直接key
        print(f"\t{key.title()}, I see you love {language}")
if "erin" not in favorite_languages.keys():
        print("Erin, please take our poll!")

