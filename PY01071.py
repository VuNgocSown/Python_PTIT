if(__name__=='__main__'):
    s = input()
    s = s.lower()
    if(s[len(s)-3:]=='.py'):
        print("yes")
    else:
        print("no")