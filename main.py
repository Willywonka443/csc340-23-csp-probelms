from constraint import Problem


def coloring_map():
    # Part 1 - we will do this together in class.
    pass
    p = Problem()
    p.addVariable("WA",["Red","Green","Blue"])
    p.addVariable("NT",["Red","Green","Blue"])
    p.addVariable("SA",["Red","Green","Blue"])
    p.addVariable("Q",["Red","Green","Blue"])
    p.addVariable("NSW",["Red","Green","Blue"])
    p.addVariable("V",["Red","Green","Blue"])
    p.addVariable("T",["Red","Green","Blue"])

    s1 = p.getSolution()
    print(s1)

    
    p.addConstraint(lambda a,b: a != b, ("WA", "NT"))
    p.addConstraint(lambda a,b: a != b, ("WA", "SA"))
    p.addConstraint(lambda a,b: a != b, ("SA", "Q"))
    p.addConstraint(lambda a,b: a != b, ("SA", "NSW"))
    p.addConstraint(lambda a,b: a != b, ("SA", "V"))
    p.addConstraint(lambda a,b: a != b, ("NT", "SA"))
    p.addConstraint(lambda a,b: a != b, ("Q", "NT"))
    p.addConstraint(lambda a,b: a != b, ("Q", "NSW"))
    p.addConstraint(lambda a,b: a != b, ("NSW", "V"))
    
    s2 = p.getSolution()
    print(s2)


def scheduling_problem():
    # Look at "Part 2" instructions and do that here.
    pass
    p = Problem()
    p.addVariable("A",["Mon","Wed","Fri"])
    p.addVariable("B",["Mon","Tue"])
    p.addVariable("C",["Tue","Wed","Thu","Fri"])
    p.addVariable("D",["Mon","Wed","Fri"])
    p.addVariable("E",["Wed","Thu","Fri"])

    s1 = p.getSolution()
    print(s1)
    
    p.addConstraint(lambda a,b: a != b, ("D", "C"))
    p.addConstraint(lambda a,b: a != b, ("D", "E"))
    p.addConstraint(lambda a,b: a != b, ("D", "A"))
    p.addConstraint(lambda a,b: a != b, ("B", "C"))
    p.addConstraint(lambda a,b: a == b, ("B", "A"))
    p.addConstraint(lambda a,b,c: a == b or c,  ("E","B", "C"))
    

    s2 = p.getSolution()
    print(s2)

def main():
  coloring_map()
  scheduling_problem()
  

if __name__ == "__main__":
  main()