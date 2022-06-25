import subprocess
#getting metadata
meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

#decoding metadata
data = meta_data.decode('utf-8', errors ="backslashreplace")

#splitting the data line by line
data = data.split('\n')

#Creating A List Of Profiles
profiles = []

#transverse the data
for i in data:

    #find all user profile in each item
    if "All User Profile" in i:
        #if found split the item
        i = i.split(":")

        #item at index 1 will be the wifi name
        i = i[1]

        #formatting the name
        #first and last character is use less
        i = i[1:-1]

        #appending the wifi name in the list
        profiles.append(i)

#printing heading
table_header = "{:<30}| {:<}".format("Wi-Fi Name", "Password")
print(table_header)
print("-" * len(table_header))

#transversing the profiles
for i in profiles:
    # try catch block begins
    # try block
    try:
        #getting metadata with password using wifi name
        # results = subprocess.getoutput(['netsh', 'wlan', 'show', 'profiles', f'name=\"{i}\"', 'key=clear'])
        results = subprocess.getoutput(f'netsh wlan show profiles name="{i}" key=clear')
        
        #decoding and spliting data line by line
        #results = results.decode('utf-8', errors = "backslashreplace")
        results = results.split('\n')

        #finding password from the result list
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    
        #if there is password it will print the password
        try:
            print("{:<30}| {:<}".format(i, results[0]))

        #else it will print blank in front of the password
        except IndexError:
            print("{:<30}| {:<}".format(i, ""))

    # called when this process get failed
    except subprocess.CalledProcessError:
        print("Encoding Error Occured")
