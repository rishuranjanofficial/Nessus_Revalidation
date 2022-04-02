#Nessus_Revalidation_v0.1
if __name__ == '__main__':
    try:
        assessment_csv= input("Enter the Nessus's assessment CSV: ")
        revalidation_csv=input("Enter the Nessus's revalidation CSV: ")
        with open(assessment_csv, 'r') as ta, open(revalidation_csv, 'r') as tr:
            fileass = ta.readlines()
            filerev = tr.readlines()
 
        with open('remaining.csv', 'w') as outFile:
            for line in fileass:
                if line not in filerev: 
                    outFile.write(line)
        print("Open issues after revalidation are stored in \"remaining.csv\" as shown below\n\n")
        with open('remaining.csv', 'r') as tnp:
            for line in tnp:
                print(line)   
        ta.close()
        tr.close()
        outFile.close()
        tnp.close()                       
    except e:
        print(e+"Invalid CSV")
