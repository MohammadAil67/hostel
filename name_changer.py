import pickle

def filesearch():
    filename = 'file4.pkl'
    file = open(filename,'rb')
    arrayfile = file.readline().strip()
    return arrayfile


def filewrite(array):
    filename = "file4.pkl"
    file = open(filename, 'wb')
    pickle.dump(array, file)
    file.close()
            
    

name = str(input("give your name to search "))
array = filesearch()


for i in range(len(array)):
    if array[i] == name:
        print(f'here is your name {array[i]}')


change = input('Do you want to change your name?[yes/no] ').upper()

if change == 'YES':
    realname = input("Give your real name ")
    for i in range(len(array)):
        if array[i] == name:
            array.remove(i)
            array.append(realname)
            filewrite(array)


elif change == "NO":
    print("Okay")
    
        










