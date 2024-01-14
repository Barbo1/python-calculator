#  __________
# │Calculator│ 
#  ¯¯¯¯¯¯¯¯¯¯
# For:
#   - Arithmetic operators
#   - Functions operations
#   - Costants(e, π)
#   - Polynomial 1st and 2nd degree(O.O ,roots and function sign)
#

import re
from sympy.abc import x
from math import pi, sqrt, e, factorial, cos, sin, tan, acos, asin, atan, log, log10

simbols_change = [{"sim":"π", "rem":"pi"}, {"sim":"√", "rem":"sqrt"}, {"sim":"^", "rem":"**"}, {"sim":"sin¯¹", "rem":"asin"},
                  {"sim":"cos¯¹", "rem":"acos"},  {"sim":"tan¯¹", "rem":"atan"}, {"sim":"log", "rem":"log10"}, {"sim":"ln", "rem":"log"}]
message_Error = "Invalid Syntax"
message_PolyNotation = "ax^2 + bx - c"

#___________________________________________________________________________________________________________________________________________

def polyTerms(polyin):

    #--initialize variables--
    parente = 0
    ret1 = []
    terms = [] 

    #--if is between parenthesis--
    for x in range(0, len(polyin)):
        if polyin[x] == "(":
            parente += 1
        elif polyin[x] == ")":
            parente -= 1
        if (polyin[x] == "-" or polyin[x] == "+") and parente == 0:
            if x != 0:
                ret1.append(x)    

    ret1.append(len(polyin))  

    #--separate terms--
    for y in range(len(ret1)):
        if y == 0:
            terms.append(str(polyin[0:ret1[y]]))
        elif y > 0:
            terms.append(str(polyin[ret1[y-1]:ret1[y]]))
    return terms

#___________________________________________________________________________________________________________________________________________

def polyRoot(polyin):

    #--initialize variables--
    resul = []
    terms = polyTerms(polyin)
    count = 0

    #--determine terms--
    for ter in terms:
        if ter.find("x") == -1: # independent term
            count+=1
        if ter.find("x") != -1 and ter.find("x**2") == -1: # degree 1
            count+=2
        if ter.find("x**2") != -1: # degree 2
            count+=4
    for n in range(len(terms)):
        terms[n] = str(eval(terms[n].replace("x", "1")))
    
    #--Out of margin--
    if count > 7:
        return resul

    #--Degree 2 Complete--
    elif count == 7:
        if terms[1][0] == "-":
            terms[1] = terms[1][1:]
        else:
            terms[1] = "-" + terms[1]
        
        aux = "("+terms[1]+")**2 - 4*("+terms[0]+")*("+terms[2]+")"
        aux = eval(aux) 
        
        if aux >= 0:
            aux = str(sqrt(aux))
        else:
            aux = str(sqrt(-aux))+"j"
        res1 = eval("("+terms[1]+"+("+aux+"))/("+terms[0]+"*2)")
        res2 = eval("("+terms[1]+"-("+aux+"))/("+terms[0]+"*2)")
        resul.append(res2)
        resul.append(res1)

    #--degree 2-degree 1--
    elif count == 6:
        resul.append(eval("("+terms[1]+"*-1)/"+terms[0]))  
        resul.append(0)

    #--degree 2-independent term--
    elif count == 5:
        aux = eval("("+terms[1]+"*-1)/"+terms[0])
        
        if aux >= 0:
            aux = sqrt(aux)
        else:
            aux = sqrt(-aux)*j
        resul.append(aux)
        resul.append(-aux)

    #--degree 2--
    elif count == 4:
        resul.append(0)
        resul.append(0)

    #--degree 1-independent term--
    elif count == 3:
        resul.append(eval("("+terms[1]+"*-1)/"+terms[0]))

    #--degree 1--
    elif count == 2:
        resul.append(0)

    return resul

#___________________________________________________________________________________________________________________________________________

def calculate(operation):
    
    operation = "0+" + operation

    #--initialize variable--
    parenthesis = 0
    result = ""
    
    #try:
    for n in operation:
        if n == "(":
            parenthesis += 1
        elif n == ")":
            parenthesis -= 1

        if parenthesis < 0:
            raise Exception

    if parenthesis == 0:

        #--add * in 123x o x123--
        if re.search(r"\d+x", operation):
            num1 = re.sub(r"\d+x", "{}", operation)
            num2 = re.findall(r"(\d+)x", operation)
            for n in range(len(num2)):
                num2[n] = num2[n]+"*x"
            operation = num1.format(*num2)
        if re.search(r"x\d+", operation):
            num1 = re.sub(r"x\d+", "{}", operation)
            num2 = re.findall(r"x(\d+)", operation)
            for n in range(len(num2)):
                num2[n] = "x*"+num2[n]
            operation = num1.format(*num2)
        
        #--change symbols-- 
        for n in simbols_change:
            operation = operation.replace(n["sim"], n["rem"])

         #--Factorial--
        if operation.find("!"):
            num1 = re.sub(r"\!\d+", "{}", operation)
            num2 = re.findall(r"\!(\d+)", operation)
            operation = num1.format(*[factorial(eval(n)) for n in num2])

        operation = str(eval(operation))

        if not re.search("x", operation):
            return operation
        else:
            #--Simplify--
            operation_disposable = operation
            for n in simbols_change:
                operation_disposable = operation_disposable.replace(n["rem"], n["sim"])
            result = "simplified : {}".format(operation_disposable)

            #--Roots--
            roots = polyRoot(operation)
            
            result += "\nroots : r0 = " + str(roots[0]) 
            if len(roots) == 2:
                result += ", r1 = " + str(roots[1]) 
            return result

    raise Exception

    #--Exceptions control--
    #except ValueError as err:
    #    return str(err).title()
    #except Exception:
    #    return message_Error

